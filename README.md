# timberPlayer2.0

> A Python bot that plays the **Timberman** arcade game automatically by reading screen pixels and firing synthetic mouse clicks. No ML, no game-memory hooks — just fast, dumb color polling.

## ▶️ Demo

[![Python bot plays Timberman](http://img.youtube.com/vi/ewNVKUyc3RU/0.jpg)](https://www.youtube.com/watch?v=ewNVKUyc3RU)

**Watch on YouTube →** https://www.youtube.com/watch?v=ewNVKUyc3RU

## How it works

1. **Capture** — `PIL.ImageGrab` grabs a fixed region of the screen where the game is running.
2. **Sense** — `im.getpixel()` at two coordinates above the lumberjack (`lTree`, `rTree`) returns RGB tuples that are compared against the known "branch" / "no branch" colors.
3. **Act** — `win32api.mouse_event` fires a synthetic `LEFTDOWN` / `LEFTUP` on the correct side coordinate.
4. **Loop** — repeats until a "Game Over" color is detected at a known pixel; a `ColorNotFound` exception bails out and prints the final score.

To keep Python's recursion stack from blowing up on long runs, the bot throws a custom `IterationLimit` every 150 clicks and restarts itself from the current side.

## Stack

- **Python 3**
- **Pillow** (`PIL.ImageGrab`) — screen capture
- **pywin32** (`win32api`, `win32con`) — synthetic mouse events
- Tuned for **1920×1080 Windows 8** running the [Timberman browser build](http://goo.gl/6v7nM6). Coordinates are hardcoded and need re-calibration for any other setup.

## Run it

```bash
pip install pillow pywin32
python timberPlayer_2.0.py
```

Before launching:
1. Open the Timberman game and position the window where the script expects it.
2. If your resolution or browser chrome differs from the original, use the `getCoords()` helper to re-measure `x_pad` / `y_pad` and the click anchors.

## Files

| File | Purpose |
|------|---------|
| `timberPlayer_2.0.py` | Final bot — exception-driven control flow, score tracking, game-over detection. |
| `code.py` | Earlier draft kept for reference (color logic before exceptions were introduced). |
| `quickGrab.pyw` | Small utility to capture the play area for tuning new coordinates. |
| `img/`, `Record/` | Sample frames captured during development for color calibration. |

## Known limitations

- **Windows-only** — uses `win32api`.
- **Hardcoded screen coordinates** — no auto-detection of the game window.
- The bot can outrun the game's animation in long runs; the periodic `IterationLimit` reset is a workaround, not a real fix.

## Why this exists

A weekend project to learn `Pillow` and `pywin32` end-to-end while building something visually satisfying. The YouTube demo picked up enough views that the repo stays public as a "shipped and watched" side project.
