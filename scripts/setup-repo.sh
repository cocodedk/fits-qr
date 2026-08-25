#!/bin/sh
# Apply repository merge settings and branch protection on the default branch.
#
# Run ONCE, after the first CI run has completed — the required status check can only
# be registered against a context GitHub has already seen.
#
#     bash scripts/setup-repo.sh
#
# Needs the gh CLI authenticated with admin rights on the repo.
set -eu

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
DEFAULT_BRANCH=$(gh repo view --json defaultBranchRef -q .defaultBranchRef.name)
OWNER=$(gh repo view --json owner -q .owner.login)

echo ""
echo "=== Repository setup: $REPO ==="
echo ""

gh repo edit "$REPO" \
  --delete-branch-on-merge \
  --enable-squash-merge \
  --enable-rebase-merge \
  --enable-merge-commit=false

echo "✓ Merge strategy: squash + rebase only, auto-delete head branches"

# Solo-maintainer defaults: a PR is required so CI runs before merge, but zero
# approvals are needed, so you can merge your own PR. "verify" is the job name in
# .github/workflows/ci.yml — rename both together.
PROTECTION_PAYLOAD='{
  "required_status_checks": {
    "strict": true,
    "contexts": ["verify"]
  },
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": false,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 0
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": false,
  "required_conversation_resolution": false,
  "lock_branch": false,
  "block_creations": false
}'

set +e
PROT_RESP=$(printf '%s' "$PROTECTION_PAYLOAD" | gh api \
  --method PUT \
  "/repos/$REPO/branches/$DEFAULT_BRANCH/protection" \
  --input - 2>&1)
PROT_RC=$?
set -e

if [ "$PROT_RC" -eq 0 ]; then
  echo "✓ Branch protection set on $DEFAULT_BRANCH"
elif echo "$PROT_RESP" | grep -q "Upgrade to GitHub Pro"; then
  echo "⚠  Branch protection skipped — private repo on GitHub Free."
  echo "   The local pre-push hook is then the only guard; keep it installed"
  echo "   (bash scripts/install-hooks.sh) on every clone."
else
  echo "✗ Branch protection failed:" >&2
  echo "$PROT_RESP" >&2
  exit 1
fi

mkdir -p .github
printf '# All files — the repo owner is auto-requested for review on every PR.\n* @%s\n' \
  "$OWNER" > .github/CODEOWNERS
echo "✓ .github/CODEOWNERS written"

echo ""
echo "Active on $DEFAULT_BRANCH:"
if [ "$PROT_RC" -eq 0 ]; then
  echo "  - CI job 'verify' must pass before merge"
  echo "  - PR required, 0 approvals (self-merge is fine)"
  echo "  - No force pushes, no branch deletion"
  echo "  - Admins can bypass in an emergency"
else
  echo "  - No server-side protection; the pre-push hook is the only guard"
fi
echo ""
