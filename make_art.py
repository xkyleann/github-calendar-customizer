#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════╗
║         GitHub Contribution Art Maker         ║
║         github.com/xkyleann                   ║
╚═══════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime, timedelta

# ── ANSI colors ──────────────────────────────────────────────────────────────
R = "\033[0m"
BOLD = "\033[1m"
G0 = "\033[38;5;235m"  # empty
G1 = "\033[38;5;22m"   # level 1
G2 = "\033[38;5;28m"   # level 2
G3 = "\033[38;5;34m"   # level 3
G4 = "\033[38;5;46m"   # level 4
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[97m"

LEVEL_COLORS = [G0, G1, G2, G3, G4]
LEVEL_BLOCKS = ["░░", "▒▒", "▓▓", "██", "██"]

# ── Patterns (7 rows = Sun→Sat, cols = weeks) ────────────────────────────────
PATTERNS = {
    "kitty": {
        "name": "Kitty Cat 🐱",
        "grid": [
            [0,0,4,4,4,0,0],
            [0,4,4,4,4,4,0],
            [4,4,2,4,2,4,4],
            [4,4,4,4,4,4,4],
            [4,2,4,4,4,2,4],
            [0,4,4,4,4,4,0],
            [0,0,4,0,4,0,0],
            [0,0,4,0,4,0,0],
            [0,0,0,0,0,0,0],
        ],
    },
    "heart": {
        "name": "Heart ❤️",
        "grid": [
            [0,3,3,0,3,3,0],
            [3,4,4,3,4,4,3],
            [3,4,4,4,4,4,3],
            [3,4,4,4,4,4,3],
            [0,3,4,4,4,3,0],
            [0,0,3,4,3,0,0],
            [0,0,0,3,0,0,0],
        ],
    },
    "wave": {
        "name": "Wave 🌊",
        "grid": [
            [0,0,2,0,0,2,0,0,2,0,0,2,0],
            [0,2,3,2,0,2,3,2,0,2,3,2,0],
            [2,3,4,3,2,3,4,3,2,3,4,3,2],
            [3,4,4,4,3,4,4,4,3,4,4,4,3],
            [2,3,4,3,2,3,4,3,2,3,4,3,2],
            [0,2,3,2,0,2,3,2,0,2,3,2,0],
            [0,0,2,0,0,2,0,0,2,0,0,2,0],
        ],
    },
    "pac": {
        "name": "Pac-Man 👾",
        "grid": [
            [0,0,4,4,4,0,0],
            [0,4,4,4,4,4,0],
            [4,4,4,0,0,0,0],
            [4,4,4,0,0,0,0],
            [4,4,4,0,0,0,0],
            [0,4,4,4,4,4,0],
            [0,0,4,4,4,0,0],
            [0,0,0,0,0,0,0],
            [0,0,4,0,0,4,0],
        ],
    },
    "diamond": {
        "name": "Diamond 💎",
        "grid": [
            [0,0,0,4,0,0,0],
            [0,0,4,4,4,0,0],
            [0,4,4,4,4,4,0],
            [4,4,3,2,3,4,4],
            [0,4,4,4,4,4,0],
            [0,0,4,4,4,0,0],
            [0,0,0,4,0,0,0],
        ],
    },
    "xkyleann": {
        "name": "xkyleann text ✍️",
        "grid": [
            # X     K     Y     L     E     A     N     N
            [4,0,4, 4,0,4, 4,0,4, 4,0,0, 4,4,4, 0,4,0, 4,0,4, 4,0,4],
            [4,0,4, 4,0,4, 4,0,4, 4,0,0, 4,0,0, 4,4,0, 4,4,4, 4,4,4],
            [0,4,0, 4,4,0, 0,4,0, 4,0,0, 4,4,0, 4,0,4, 4,0,4, 4,0,4],
            [0,4,0, 4,0,4, 0,4,0, 4,0,0, 4,0,0, 4,4,4, 4,0,4, 4,0,4],
            [4,0,4, 4,0,4, 0,4,0, 4,0,0, 4,4,4, 0,0,4, 4,0,4, 4,0,4],
            [4,0,4, 4,0,4, 0,4,0, 4,4,4, 4,0,0, 0,0,4, 4,0,4, 4,0,4],
            [4,0,4, 4,0,4, 0,4,0, 4,4,4, 4,4,4, 0,0,4, 4,0,4, 4,0,4],
        ],
    },
    "custom": {
        "name": "Custom pattern",
        "grid": [],
    },
}

# ── Helpers ───────────────────────────────────────────────────────────────────
def clear(): os.system("clear" if os.name == "posix" else "cls")

def banner():
    print(f"""{CYAN}{BOLD}
  ╔═══════════════════════════════════════════════╗
  ║    GitHub Contribution Graph Art Maker 🎨     ║
  ║    github.com/xkyleann                        ║
  ╚═══════════════════════════════════════════════╝{R}
""")

def preview_pattern(grid, label="preview"):
    cols = len(grid)
    rows = len(grid[0]) if cols else 0
    print(f"\n  {YELLOW}{BOLD}{label}{R}")
    print(f"  {WHITE}{'  '.join(['S','M','T','W','T','F','S'])}{R}")
    for r in range(rows):
        sys.stdout.write("  ")
        for c in range(cols):
            val = grid[c][r]
            color = LEVEL_COLORS[val]
            block = LEVEL_BLOCKS[val]
            sys.stdout.write(f"{color}{block}{R}")
        print()
    print(f"\n  {WHITE}cols: {cols}  rows: {rows}{R}")

def run(cmd, cwd=None, silent=False):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if not silent and result.stdout.strip():
        print(f"  {result.stdout.strip()}")
    if result.returncode != 0 and result.stderr.strip() and "already exists" not in result.stderr:
        print(f"  {RED}{result.stderr.strip()}{R}")
    return result

def progress_bar(current, total, width=40):
    pct = current / total
    filled = int(width * pct)
    bar = "█" * filled + "░" * (width - filled)
    color = G4 if pct > 0.66 else G2 if pct > 0.33 else G1
    sys.stdout.write(f"\r  {color}[{bar}]{R} {WHITE}{current}/{total}{R} commits  ")
    sys.stdout.flush()

def get_start_date(year, offset_weeks=0):
    jan1 = datetime(year, 1, 1, 12, 0, 0)
    days_to_sunday = (6 - jan1.weekday()) % 7
    start = jan1 + timedelta(days=days_to_sunday) + timedelta(weeks=offset_weeks)
    return start

def build_commit_dates(grid, start, commits_per_level):
    dates = []
    cols = len(grid)
    rows = len(grid[0]) if cols else 0
    for c in range(cols):
        for r in range(rows):
            val = grid[c][r]
            if val == 0:
                continue
            date = start + timedelta(weeks=c, days=r)
            count = commits_per_level[val]
            dates.extend([date] * count)
    dates.sort()
    return dates

def choose_pattern():
    print(f"\n  {YELLOW}{BOLD}Available patterns:{R}\n")
    keys = list(PATTERNS.keys())
    for i, k in enumerate(keys):
        print(f"  {CYAN}[{i+1}]{R} {PATTERNS[k]['name']}")
    print()
    while True:
        try:
            choice = int(input(f"  {WHITE}Choose a pattern (1-{len(keys)}): {R}")) - 1
            if 0 <= choice < len(keys):
                key = keys[choice]
                if key == "custom":
                    return get_custom_pattern()
                return key, PATTERNS[key]["grid"]
        except (ValueError, KeyboardInterrupt):
            pass
        print(f"  {RED}Invalid choice, try again.{R}")

def get_custom_pattern():
    print(f"""
  {YELLOW}Custom pattern editor{R}
  Enter your grid row by row (7 rows, Sun→Sat).
  Use 0 (empty) to 4 (darkest), space-separated.
  Example: 0 4 4 4 4 4 0

  How many columns wide? """, end="")
    cols = int(input())
    rows = 7
    grid = []
    for c in range(cols):
        col = []
        for r in range(rows):
            while True:
                try:
                    raw = input(f"  col {c+1}, row {r+1} (0-4): ")
                    val = int(raw.strip())
                    if 0 <= val <= 4:
                        col.append(val)
                        break
                except ValueError:
                    pass
        grid.append(col)
    return "custom", grid

def main():
    clear()
    banner()

    # ── Get GitHub info ───────────────────────────────────────────────────────
    print(f"  {YELLOW}{BOLD}Step 1 — GitHub account{R}\n")
    username = input(f"  {WHITE}GitHub username: {R}").strip()
    email = input(f"  {WHITE}GitHub noreply email\n  (e.g. 123456+{username}@users.noreply.github.com): {R}").strip()
    repo = input(f"  {WHITE}Repo name [{username}-art]: {R}").strip() or f"{username}-art"

    # ── Choose pattern ────────────────────────────────────────────────────────
    print(f"\n  {YELLOW}{BOLD}Step 2 — Choose your pattern{R}")
    pattern_key, grid = choose_pattern()
    preview_pattern(grid, PATTERNS[pattern_key]["name"])

    # ── Choose year ───────────────────────────────────────────────────────────
    print(f"\n  {YELLOW}{BOLD}Step 3 — Year{R}\n")
    current_year = datetime.now().year
    year_input = input(f"  {WHITE}Year to draw on [{current_year - 1}]: {R}").strip()
    year = int(year_input) if year_input.isdigit() else current_year - 1

    offset_input = input(f"  {WHITE}Week offset from start [0]: {R}").strip()
    offset = int(offset_input) if offset_input.isdigit() else 0

    # ── Intensity ─────────────────────────────────────────────────────────────
    print(f"\n  {YELLOW}{BOLD}Step 4 — Commit intensity{R}\n")
    print(f"  {WHITE}How many commits per level? (more = darker squares){R}")
    intensity_input = input(f"  {WHITE}Commits per level [2]: {R}").strip()
    base = int(intensity_input) if intensity_input.isdigit() else 2
    commits_per_level = {0: 0, 1: base, 2: base*2, 3: base*3, 4: base*4}

    # ── Summary ───────────────────────────────────────────────────────────────
    start = get_start_date(year, offset)
    dates = build_commit_dates(grid, start, commits_per_level)

    print(f"""
  {CYAN}{'─'*47}{R}
  {WHITE}username:{R}  {username}
  {WHITE}email:{R}     {email}
  {WHITE}repo:{R}      {repo}
  {WHITE}pattern:{R}   {PATTERNS[pattern_key]['name']}
  {WHITE}year:{R}      {year} (starting {start.strftime('%b %d, %Y')})
  {WHITE}commits:{R}   {len(dates)}
  {CYAN}{'─'*47}{R}
""")
    confirm = input(f"  {WHITE}Looks good? Press Enter to start, or Ctrl+C to cancel: {R}")

    # ── Setup repo ────────────────────────────────────────────────────────────
    print(f"\n  {YELLOW}{BOLD}Step 5 — Creating repo and commits...{R}\n")
    repo_path = os.path.join(os.getcwd(), repo)
    os.makedirs(repo_path, exist_ok=True)

    run("git init", cwd=repo_path, silent=True)
    run(f'git config user.email "{email}"', cwd=repo_path, silent=True)
    run(f'git config user.name "{username}"', cwd=repo_path, silent=True)

    readme = os.path.join(repo_path, "README.md")
    with open(readme, "w") as f:
        f.write(f"# {repo}\n\npixel art on the GitHub contribution graph 🎨\npattern: {PATTERNS[pattern_key]['name']}\n")
    run("git add README.md", cwd=repo_path, silent=True)

    # ── Make commits ──────────────────────────────────────────────────────────
    for i, date in enumerate(dates):
        date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
        env = f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}"'
        run(f'{env} git commit --allow-empty -m "🎨" --quiet', cwd=repo_path, silent=True)
        progress_bar(i + 1, len(dates))

    print(f"\n\n  {G4}✓ {len(dates)} commits created!{R}")

    # ── Set remote ────────────────────────────────────────────────────────────
    repo_url = f"https://github.com/{username}/{repo}.git"
    run("git remote remove origin", cwd=repo_path, silent=True)
    run(f"git remote add origin {repo_url}", cwd=repo_path, silent=True)
    run("git branch -M main", cwd=repo_path, silent=True)

    # ── Done ──────────────────────────────────────────────────────────────────
    print(f"""
  {CYAN}{'─'*47}{R}
  {G4}{BOLD}All done! Now push to GitHub:{R}

  {WHITE}cd {repo}{R}
  {WHITE}git push origin main --force{R}

  {WHITE}Use your Personal Access Token as the password.{R}
  {WHITE}Generate one at: github.com → Settings →{R}
  {WHITE}Developer settings → Personal access tokens{R}

  {WHITE}Then check your profile at:{R}
  {CYAN}https://github.com/{username}{R}
  {WHITE}Click {year} on the right side of the graph.{R}
  {CYAN}{'─'*47}{R}
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {RED}Cancelled.{R}\n")
