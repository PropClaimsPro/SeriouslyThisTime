#!/bin/bash
# Auto-push latest app to GitHub repo

REPO_NAME="SeriouslyThisTime"
GIT_URL="git@github.com:YOUR_USERNAME/${REPO_NAME}.git"

echo "[+] Initializing Git repo and pushing to ${REPO_NAME}..."

git init
git remote add origin $GIT_URL
git add .
git commit -m "🚀 Final MAX-FUSION Autonomous Profit App Upload"
git branch -M main
git push -u origin main

echo "[✔] Push complete. Trigger DigitalOcean deployment now."