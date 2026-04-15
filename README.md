<div align="center">

# ᓚᘏᗢ github contribution art maker

**draw pixel art on your github graph with a single python script ✨**

```
░░████░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████░   ░░██░░██░░██░░██░░░░░░██░░░░░░░░░░██░░░░░░░
████████   ░██░░░██░░██░░██░░░░░░██░░░░░░░░░░██░░░░░░░
██░░░░██   ░████░████░░████░░░░░░██░░░░░░░░░░██░░░░░░░
████████   ░██░░░██░██░░░██░░░░░░██░░░░░░░░░░██░░░░░░░
░██████░   ░░██░░██░░██░░██░░░░░░████░░░░░░░░████░░░░░
░░░██░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░██░░░
```

[![made with love](https://img.shields.io/badge/made%20with-%E2%99%A1-ff69b4?style=flat-square)](https://github.com/xkyleann)
[![python](https://img.shields.io/badge/python-3.6+-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![contributions](https://img.shields.io/badge/contributions-fake%20but%20cute-brightgreen?style=flat-square)](https://github.com/xkyleann)

</div>

---

## ✦ what is this (◕ᴗ◕✿)

your github contribution graph is just a grid of green squares.  
each square = a day you made a commit.  
this script makes **backdated commits** to draw pixel art on it. simple as that ˙ᵕ˙

---

## ✦ quickstart ⟡

```bash
git clone https://github.com/xkyleann/github-calendar-customizer.git
cd github-calendar-customizer
python make_art.py
```

just follow the prompts! then push:

```bash
cd your-new-repo
git push origin main --force
```

done ✔︎ check your github profile and click the year on the right ♡

---

## ✦ patterns included ˚₊‧꒰ა ☆ ໒꒱ ‧₊˚

| pattern | preview |
|---------|---------|
| 🐱 `kitty` | a lil cat with ears, eyes and paws |
| 🌊 `wave` | repeating wave across the whole graph |
| ❤️ `heart` | classic heart shape |
| 👾 `pac` | pac-man |
| 💎 `diamond` | shaded diamond |
| ✍️ `xkyleann` | pixel text |
| 🎨 `custom` | draw your own cell by cell |

---

## ✦ before you run — important! ⚠️

your git email must match your github noreply email or commits won't show up on your graph (╥_╥)

find it at: **github → settings → emails**  
it looks like this:
```
123456789+yourusername@users.noreply.github.com
```

for pushing, use a **personal access token** as your password — not your real github password!  
get one at: **github → settings → developer settings → personal access tokens → tokens (classic)**  
check the `repo` scope ✓

---

## ✦ how the grid works ⊹ ࣪ ˖

patterns are lists of columns, each column has 7 values (sunday → saturday):

```python
# 0 = empty   1 = ░ lightest   2 = ▒   3 = ▓   4 = █ darkest
KITTY = [
    [0, 0, 4, 4, 4, 0, 0],   # col 0
    [0, 4, 4, 4, 4, 4, 0],   # col 1
    [4, 4, 2, 4, 2, 4, 4],   # col 2  ← eyes!
    ...
]
```

---

## ✦ faq ˘ᵕ˘

**will this get my account banned?**  
no, it's just commits. github doesn't care.

**can i undo it?**  
yes! just delete the repo and the squares disappear.

**why aren't my commits showing?**  
your email doesn't match. double check your noreply email!

**can i draw on multiple years?**  
yes! run the script again with a different year.

---

## ✦ credits ♡

inspired by [gitfiti](https://github.com/gelstudios/gitfiti) and [github-calendar-customizer](https://github.com/ZachSaucier/github-calendar-customizer)

made with ♡ by [@xkyleann](https://github.com/xkyleann)

---

<div align="center">

*if this made your github prettier, leave a ⭐ (´｡• ᵕ •｡`) ♡*

</div>
