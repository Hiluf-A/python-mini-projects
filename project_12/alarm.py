import winsound
from pathlib import Path
import time
import sys


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds: int) -> None:
    print(CLEAR, end="")
    start = time.time()

    while True:
        elapsed = int(time.time() - start)
        remaining = max(0, seconds -elapsed)
        m, s = divmod(remaining, 60)
        print(f"{CLEAR_AND_RETURN}{m:02d}:{s:02d}", end='',flush=True)

        if remaining == 0:
            break
        time.sleep(0.1)

    sound = Path(__file__).with_name("alarm.wav")
    if not sound.exists():
        print(f"\nCound not find file at: {sound.resolve()}")
        return
    
    try:
        winsound.PlaySound(str(sound), winsound.SND_FILENAME)
    except Exception as e:
        print(f"\nPlaysound failed: {e}\n"
              f"Try conversint to WAV and using windsound as fallback.")




def get_time_duration() -> int:
    while True:
        try:
            minutes = int(input("How many minutes to wait: "))
            seconds = int(input("How many seconds to wait: "))
            if minutes < 0 or seconds < 0:
                print("Please enter non-negative values.")
                continue
            return minutes * 60 + seconds
        except ValueError:
            print("Please enter numberic values only!")



def main() -> None:
    alarm_duration = get_time_duration()
    alarm(alarm_duration) 


if __name__ == "__main__":
    main()






