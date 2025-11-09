\# Speed Typing Test (curses)



A minimal terminal typing test written in Python using `curses`. Shows live WPM, accuracy, and per-character feedback (green = correct, red = wrong). Backspace supported; press `ESC` to quit.



\## Features

\- Live \*\*WPM\*\* and \*\*accuracy\*\*

\- Real-time per-char color feedback

\- Non-blocking input for smooth updates

\- Simple, single-file script



\## Requirements

\- Python 3.8+

\- Linux/macOS terminal with `curses` available  

\- \*\*Windows:\*\* `pip install windows-curses`



\## Installation

```bash

git clone https://github.com/Hiluf-A/python-mini-projects

cd python-mini-projects

\# Windows only:

pip install windows-curses

Usage

python typing\_speed.py





\## Controls



Type the line shown on screen



Backspace to correct



ESC to abort



\## Configuration



Open the script and edit:



TARGET\_TEXT – the sentence to type

(You can also adapt the code to load random lines from a file.)



How WPM is computed



WPM uses the common formula:

(typed\_chars / 5) / minutes\_elapsed



\## Troubleshooting



Terminal looks “broken” after a crash: run reset (Linux/macOS) or close/reopen the terminal (Windows).



On Windows: if import curses fails, run pip install windows-curses.



If your terminal is narrower than the target text, characters may clip; resize or shorten the text.



\## Roadmap (ideas)



Timed mode (e.g., 60s test)



Random passages / difficulty levels



Progress bar, caret, detailed stats (errors, net/gross WPM)



Save best scores to JSON (leaderboard)





