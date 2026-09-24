#!/usr/bin/env python3
"""Scroll the mouse wheel on a timer, so infinite-scroll pages load to the end.

Point the mouse at the page (a long YouTube search, a feed, a store listing),
start the script, and stop it with Ctrl+C.
"""
import argparse
import sys
import time

try:
    from pynput.mouse import Controller
except ImportError:
    sys.exit("auto-scroll needs pynput:  pip install pynput")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("-i", "--interval", type=float, default=0.25, help="seconds between scrolls (default 0.25)")
    p.add_argument("-a", "--amount", type=int, default=-1, help="wheel steps per scroll; negative scrolls down (default -1)")
    p.add_argument("-d", "--delay", type=float, default=3, help="seconds to wait before starting (default 3)")
    p.add_argument("-t", "--time", type=float, default=0, help="stop after this many seconds (default: run until Ctrl+C)")
    args = p.parse_args()

    mouse = Controller()
    print(f"Starting in {args.delay:g} s. Put the pointer over the page. Ctrl+C to stop.")
    time.sleep(args.delay)
    end = time.monotonic() + args.time if args.time else None
    try:
        while end is None or time.monotonic() < end:
            mouse.scroll(0, args.amount)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        pass
    print("Stopped.")


if __name__ == "__main__":
    main()
