#!/bin/bash
set -e

# Detect package manager
if [ -x "$(command -v pacman)" ]; then
    PKG_MANAGER="pacman"
elif [ -x "$(command -v apt-get)" ]; then
    PKG_MANAGER="apt-get"
else
    echo "Error: Neither pacman nor apt-get found. Cannot proceed."
    exit 1
fi

# Install PostgreSQL based on package manager
if [ "$PKG_MANAGER" = "pacman" ]; then
    $PKG_MANAGER -Sy --noconfirm postgresql
    $PKG_MANAGER -Sc --noconfirm  # Clean cached packages
elif [ "$PKG_MANAGER" = "apt-get" ]; then
    $PKG_MANAGER update
    $PKG_MANAGER install -y --no-install-recommends postgresql postgresql-contrib
    $PKG_MANAGER clean  # Clean cached packages
fi

echo "PostgreSQL installation completed."
