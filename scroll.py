import pyautogui
import time

def scroll_mouse(interval=0.25, scroll_amount=-1):
    """
    Scrolls the mouse wheel at a specified interval.

    Parameters:
    interval (float): Time interval between each scroll in seconds.
    scroll_amount (int): Amount to scroll. Positive values scroll up, negative scroll down.
    """
    while True:
        pyautogui.scroll(scroll_amount)
        time.sleep(interval)

if __name__ == "__main__":
    scroll_mouse(interval=0.25, scroll_amount=-1)
