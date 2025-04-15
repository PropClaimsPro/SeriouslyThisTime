$REPO_NAME = "SeriouslyThisTime"
$GIT_URL = "git@github.com:PropClaimsPro/$REPO_NAME.git"

Write-Host "[+] Initializing Git repo and pushing to $REPO_NAME..."

git init
git remote add origin $GIT_URL
git add .
git commit -m "Initial commit: Autonomous Profit App Deployment"
git branch -M main
git push -u origin main

Write-Host "[DONE] Push complete. Trigger DigitalOcean deployment now."