#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime, timedelta

# --- Config ---
GITHUB_USERNAME = "xkyleann"
GITHUB_EMAIL = "128597547+xkyleann@users.noreply.github.com"
REPO_NAME = "github-calendar-customizer"
REPO_URL = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

# Kitty pattern — 7 rows x 9 cols (row 0 = Sunday)
# 0 = no commit, 1-4 = intensity
KITTY = [
    [0, 0, 0, 0, 0, 0, 0],  # col 0
    [0, 4, 4, 4, 4, 4, 0],  # col 1
    [4, 4, 2, 4, 2, 4, 4],  # col 2
    [4, 4, 4, 4, 4, 4, 4],  # col 3
    [4, 2, 4, 4, 4, 2, 4],  # col 4
    [0, 4, 4, 4, 4, 4, 0],  # col 5
    [0, 0, 4, 0, 4, 0, 0],  # col 6
    [0, 0, 4, 0, 4, 0, 0],  # col 7
    [0, 0, 0, 0, 0, 0, 0],  # col 8
]

# Start from ~52 weeks ago, aligned to Sunday
today = datetime.now()
days_since_sunday = today.weekday() + 1  # Mon=0, so +1 to get to Sunday
start = today - timedelta(weeks=52) - timedelta(days=days_since_sunday % 7)
start = start.replace(hour=12, minute=0, second=0, microsecond=0)

# Center the kitty horizontally (53 weeks total)
offset_weeks = (53 - len(KITTY)) // 2

# Build list of commit dates
commit_dates = []
for col_i, col in enumerate(KITTY):
    week = offset_weeks + col_i
    for row, level in enumerate(col):
        if level == 0:
            continue
        date = start + timedelta(weeks=week, days=row)
        commit_dates.extend([date] * level * 2)  # multiply for visibility

commit_dates.sort()

# --- Setup repo ---
repo_path = os.path.join(os.getcwd(), REPO_NAME)

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
    return result

print(f"Setting up repo at {repo_path}...")
os.makedirs(repo_path, exist_ok=True)

run("git init", cwd=repo_path)
run(f'git config user.email "{GITHUB_EMAIL}"', cwd=repo_path)
run(f'git config user.name "{GITHUB_USERNAME}"', cwd=repo_path)

# Create a file to commit
readme = os.path.join(repo_path, "README.md")
with open(readme, "w") as f:
    f.write(f"# {REPO_NAME}\n\nkitty on the contribution graph 🐱\n")
run("git add README.md", cwd=repo_path)

print(f"\nCreating {len(commit_dates)} commits...")
for i, date in enumerate(commit_dates):
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env = f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}"'
    run(f'{env} git commit --allow-empty -m "kitty" --quiet', cwd=repo_path)
    if (i + 1) % 50 == 0:
        print(f"  {i+1}/{len(commit_dates)} commits done...")

print("\nAll commits created!")

# Set remote
run("git remote remove origin", cwd=repo_path)
run(f"git remote add origin {REPO_URL}", cwd=repo_path)
run("git branch -M main", cwd=repo_path)

print("\nReady to push! Run this next:")
print(f"  cd {REPO_NAME}")
print(f"  git push origin main --force")
print("\nYou'll be asked for:")
print(f"  Username: {GITHUB_USERNAME}")
print(f"  Password: your Personal Access Token")
