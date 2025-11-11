import curses
from curses import wrapper
import time
import string

TARGET_TEXT = "Hello world, this is some test text for this app!"
INSTRUCTIONS = "Type the line. Backspace to correct. ESC to quit."

def start_screen(stdscr):
    stdscr.clear()
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    stdscr.addstr(0, 0, "Welcome to the Speed Typing Test!")
    stdscr.addstr(2, 0, "Press any key to begin…")
    stdscr.refresh()
    stdscr.getkey()

def compute_wpm(chars_typed, start_time):
    elapsed = max(time.time() - start_time, 0.001)
    minutes = elapsed / 60.0
    return round((chars_typed / 5.0) / minutes, 1)

def compute_accuracy(target, typed):
    if not typed:
        return 100.0
    correct = sum(1 for i, ch in enumerate(typed) if i < len(target) and ch == target[i])
    return round(100.0 * correct / len(typed), 1)

def display_text(stdscr, target_text, typed_text, wpm=0.0, acc=100.0):
    h, w = stdscr.getmaxyx()
    # Truncate to fit the window width if necessary
    max_cols = max(0, w - 1)

    # Header
    stdscr.addnstr(0, 0, target_text, max_cols)
    stdscr.addnstr(1, 0, f"WPM: {wpm}   ACC: {acc}%".ljust(max_cols), max_cols)
    stdscr.addnstr(2, 0, INSTRUCTIONS.ljust(max_cols), max_cols)

    # Overlay typed characters with color feedback
    for i, ch in enumerate(typed_text):
        if i >= max_cols:
            break
        correct = (i < len(target_text) and ch == target_text[i])
        color = curses.color_pair(1 if correct else 2)
        stdscr.addstr(0, i, ch, color)

def typing_test(stdscr, target_text):
    current = []
    start_time = time.time()

    stdscr.nodelay(True)
    try:
        curses.curs_set(1)  # show cursor while typing
    except curses.error:
        pass

    while True:
        # Stats
        wpm = compute_wpm(len(current), start_time)
        acc = compute_accuracy(target_text, current)

        # Draw
        stdscr.clear()
        display_text(stdscr, target_text, current, wpm, acc)
        stdscr.refresh()

        # Done?
        if "".join(current) == target_text:
            stdscr.nodelay(False)
            elapsed = time.time() - start_time
            return {"completed": True, "wpm": wpm, "accuracy": acc, "elapsed": elapsed}

        # Get input (non-blocking)
        try:
            key = stdscr.getkey()
        except Exception:
            time.sleep(0.01)  # avoid 100% CPU
            continue

        # Handle ESC safely
        if len(key) == 1 and ord(key) == 27:
            stdscr.nodelay(False)
            elapsed = time.time() - start_time
            return {"completed": False, "wpm": wpm, "accuracy": acc, "elapsed": elapsed}

        # Backspace variants
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if current:
                current.pop()
            continue

        # Only accept printable single characters (including space)
        if len(key) == 1 and 32 <= ord(key) <= 126:
            if len(current) < len(target_text):
                current.append(key)
        # ignore anything else (arrows, resize, F-keys, etc.)

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)  # correct
    curses.init_pair(2, curses.COLOR_RED,   -1)  # incorrect
    curses.init_pair(3, curses.COLOR_WHITE, -1)

    start_screen(stdscr)

    while True:
        result = typing_test(stdscr, TARGET_TEXT)

        stdscr.clear()
        if result["completed"]:
            msg = f"Done! WPM {result['wpm']} • ACC {result['accuracy']}% • Time {result['elapsed']:.1f}s"
        else:
            msg = "Aborted. (ESC pressed)"
        stdscr.addstr(0, 0, msg, curses.color_pair(3))
        stdscr.addstr(2, 0, "Press ENTER to try again, or ESC to quit.")
        stdscr.refresh()

        # Wait for a decision
        while True:
            key = stdscr.getkey()
            if len(key) == 1 and ord(key) == 27:
                return
            if key in ("\n", "\r", "KEY_ENTER"):
                break

if __name__ == "__main__":
    # On Windows: pip install windows-curses
    wrapper(main)

