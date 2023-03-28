# A python script that randomly moves visible windows on screen to mitigate OLED burn-in issues


usage: OLED_avoid_burnin.py [-h] [--m M] [--s S]

Move non-minimized windows randomly on screen.

options:
  -h, --help  show this help message and exit
  --m M       The maximum number of pixels to move the window in any direction
  --s S       The time to wait before moving the windows again, in seconds
