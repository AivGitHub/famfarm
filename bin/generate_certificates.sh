#!/usr/bin/env bash

# Paths
BIN_DIR="$(dirname "$BASH_SOURCE")"
PROJECT_DIR="$(dirname "$BIN_DIR")"
PROJECT_DIR_ABSOLUTE="$(readlink -f "$PROJECT_DIR")"

CERTIFICATES_PATH="$PROJECT_DIR_ABSOLUTE/internal/nginx/settings/certificates"
SERVER_KEY="$CERTIFICATES_PATH/server.key"
SERVER_CRT="$CERTIFICATES_PATH/server.crt"

# Create certificates directory if not exists
mkdir -p $CERTIFICATES_PATH

# Commands
OPENSSL_CMD="/usr/bin/openssl"

$OPENSSL_CMD req -x509 -nodes -days 365 -newkey rsa:4096 -keyout $SERVER_KEY -out $SERVER_CRT
