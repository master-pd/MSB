#!/bin/bash

echo "[1/6] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[2/6] Installing Git, Python, nano..."
pkg install git -y
pkg install python -y
pkg install nano -y

echo "[3/6] Upgrading pip..."
pip install --upgrade pip

echo "[4/6] Installing required Python libraries..."
pip install python-telegram-bot==13.15 requests

REPO_URL="https://github.com/master-pd/Spam-bot.git"
DIR_NAME="Spam-bot"

if [ -d "$DIR_NAME" ]; then
    echo "[5/6] Directory $DIR_NAME already exists. Skipping clone."
else
    echo "[5/6] Cloning repository..."
    git clone $REPO_URL
fi

cd $DIR_NAME
chmod +x main.py

echo "[6/6] Setup complete! Run with: python main.py"