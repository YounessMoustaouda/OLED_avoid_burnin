import win32gui
import win32con
import random
import time
import argparse

def move_windows(move_amount, sleep_time):
    # Get all top-level windows
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd) and not win32gui.IsIconic(hwnd):
            windows.append(hwnd)
        return True
    windows = []
    win32gui.EnumWindows(callback, windows)

    # Move each window by a random offset
    for hwnd in windows:
        x, y, w, h = win32gui.GetWindowRect(hwnd)
        x_offset = random.randint(-move_amount, move_amount)
        y_offset = random.randint(-move_amount, move_amount)
        win32gui.MoveWindow(hwnd, x + x_offset, y + y_offset, w-x, h-y, True)

    # Wait for the specified time before moving the windows again
    time.sleep(sleep_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Move non-minimized windows randomly on screen.')
    parser.add_argument('--m', type=int, help='The maximum number of pixels to move the window in any direction',default=1)
    parser.add_argument('--s', type=float, help='The time to wait before moving the windows again, in seconds',default=15)
    args = parser.parse_args()

    while True:
        try:
            move_windows(args.m, args.s)
        except:
            pass
