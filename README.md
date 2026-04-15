# 🐱 kitty on my GitHub contribution graph

Put a cat on your GitHub contribution graph using fake backdated commits.

![kitty contribution graph](https://i.imgur.com/96Ah7dw.png)

## how it works

GitHub's contribution graph shows a green square for every day you make a commit. By creating commits with backdated timestamps, you can draw pixel art on your graph.

This repo uses a custom Python script (`make_kitty.py`) to generate hundreds of backdated commits in the shape of a kitty cat.

## how to do it yourself

### 1. clone this repo
```bash
git clone https://github.com/xkyleann/github-calendar-customizer.git
cd github-calendar-customizer
```

### 2. set your git email to match your GitHub account
```bash
git config --global user.email "YOUR_GITHUB_NOREPLY_EMAIL"
git config --global user.name "YOUR_GITHUB_USERNAME"
```

Find your noreply email at: **GitHub → Settings → Emails**  
It looks like: `123456789+yourusername@users.noreply.github.com`

### 3. edit make_kitty.py
Open `make_kitty.py` and update these two lines:
```python
GITHUB_USERNAME = "your-username"
GITHUB_EMAIL = "your-noreply@users.noreply.github.com"
```

### 4. run the script
```bash
python make_kitty.py
```

### 5. push to GitHub
```bash
cd github-calendar-customizer
git remote set-url origin https://github.com/YOUR_USERNAME/github-calendar-customizer.git
git push origin main --force
```

Enter your **Personal Access Token** as the password (not your GitHub password).  
Generate one at: **GitHub → Settings → Developer settings → Personal access tokens**

### 6. check your profile
Go to your GitHub profile and click **2025** on the right side of the contribution graph. 🐱

## customize the pattern

Edit the `KITTY` array in `make_kitty.py` to draw your own pixel art.  
The grid is **7 rows** (Sun–Sat) × however many columns you want.  
Values: `0` = empty, `1–4` = green intensity (light → dark).

```python
KITTY = [
    [0, 0, 0, 0, 0, 0, 0],  # col 0
    [0, 4, 4, 4, 4, 4, 0],  # col 1
    ...
]
```

## credits

Inspired by [gitfiti](https://github.com/gelstudios/gitfiti) and [github-calendar-customizer](https://github.com/ZachSaucier/github-calendar-customizer).
