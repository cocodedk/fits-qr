#!/usr/bin/env bash
# Generate the release-signing keystore used to sign FITS-QR release APKs.
#
# Idempotent: refuses to touch an existing keystore. Creates $KEYSTORE_DIR (default
# ~/.fits-release), generates a keystore with random passwords, and writes those
# passwords (plus the key alias) to credentials.txt for scripts/setup-signing.sh to
# upload as GitHub Actions secrets.
#
# Usage: bash scripts/generate-keystore.sh
set -euo pipefail

dir="${KEYSTORE_DIR:-$HOME/.fits-release}"
keystore="$dir/release.keystore"
creds="$dir/credentials.txt"
alias_name="fits"

if [ -f "$keystore" ]; then
  echo "Keystore already exists at $keystore — refusing to overwrite." >&2
  exit 1
fi

keytool_bin="keytool"
if ! command -v keytool >/dev/null 2>&1; then
  fallback_java_home="/home/agent/jdk/jdk-17.0.19+10"
  if [ -x "$fallback_java_home/bin/keytool" ]; then
    keytool_bin="$fallback_java_home/bin/keytool"
  else
    echo "keytool not found on PATH and fallback JAVA_HOME ($fallback_java_home) has none either." >&2
    exit 1
  fi
fi

mkdir -p "$dir"
chmod 700 "$dir"

keystore_password=$(openssl rand -base64 24 | tr -d '\n=+/' | cut -c1-24)
# PKCS12 (keytool's default since JDK 9) cannot hold a key password that differs from
# the store password — it silently ignores -keypass. Keep them identical so the Gradle
# signing config, which passes both, actually opens the key.
key_password="$keystore_password"

"$keytool_bin" -genkeypair \
  -keystore "$keystore" \
  -alias "$alias_name" \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -storepass "$keystore_password" \
  -keypass "$key_password" \
  -dname "CN=FITS, O=Cocode, C=DK"

cat > "$creds" <<EOF
export KEY_ALIAS="$alias_name"
export KEYSTORE_PASSWORD="$keystore_password"
export KEY_PASSWORD="$key_password"
EOF
chmod 600 "$creds"

chmod 600 "$keystore"
echo "Keystore created at $keystore"
echo "Credentials written to $creds (chmod 600)"
echo "Next: bash scripts/setup-signing.sh"
