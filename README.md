# auto-scroll

Scroll the mouse wheel on a timer, so infinite-scroll pages load all the way to the end:
a long YouTube search, a feed, a store listing.

## Use

```sh
pip install pynput
python3 auto_scroll.py                 # scroll down every 0.25 s until Ctrl+C
python3 auto_scroll.py -i 0.5 -t 120   # every 0.5 s, stop after two minutes
python3 auto_scroll.py -a 1            # scroll up instead
```

| Option | Default | |
|---|---|---|
| `-i`, `--interval` | 0.25 | seconds between scrolls |
| `-a`, `--amount` | -1 | wheel steps per scroll; negative scrolls down |
| `-d`, `--delay` | 3 | seconds to get the pointer over the page before it starts |
| `-t`, `--time` | 0 | stop after this many seconds; 0 runs until Ctrl+C |

On macOS, give the terminal Accessibility permission so it can move the wheel.
