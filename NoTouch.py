"""
Library Documentation : https://pyautogui.readthedocs.io/en/latest/index.html ,
"""

import pyautogui
import time
import random
import pyperclip
from playsound import playsound


def find_screen_pointer():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


speed_frequency = 2

screen_size = pyautogui.size()
print(screen_size)

# find_screen_pointer()

print(input("press enter to start:"))


def open_browser():
    # find_screen_pointer()
    open_browser_move_x = 708
    open_browser_move_y = 1058
    open_browser_move = pyautogui.moveTo(open_browser_move_x, open_browser_move_y)
    time.sleep(speed_frequency)
    pyautogui.click()


open_browser()
# print(input("press enter to start:"))

# time.sleep(speed_frequency)
# pyautogui.hotkey('ctrl', 'Shift', 'M')

# time.sleep(speed_frequency)


def click_profile():
    time.sleep(speed_frequency)
    for i in range(25):
        pyautogui.hotkey('tab')
        time.sleep(0.05)
    pyautogui.hotkey('enter')


click_profile()

# print(input("press enter to Add new profile:"))


def click_sign_in():
    time.sleep(speed_frequency)
    for i in range(1):
        pyautogui.hotkey('tab')
        time.sleep(0.25)
    pyautogui.hotkey('enter')


click_sign_in()


def write_email():
    time.sleep(speed_frequency + 4)
    pyautogui.write('rabbyvip0p@gmail.com', interval=0.05)
    pyautogui.hotkey('enter')


write_email()


def write_password():
    time.sleep(speed_frequency + 4)
    pyautogui.write('globe0112358', interval=0.05)
    pyautogui.hotkey('enter')


write_password()


def click_yes_in():
    time.sleep(speed_frequency + 4)
    for i in range(1):
        pyautogui.hotkey('tab')
        time.sleep(0.25)
    pyautogui.hotkey('enter')


click_yes_in()


def maximize_chrome():
    time.sleep(speed_frequency)
    pyautogui.hotkey("Alt", "Space", "x")


maximize_chrome()

# print(input("Fix Thing :"))


def click_gmail(tab_count=1):
    time.sleep(speed_frequency)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.25)
    pyautogui.hotkey('enter')


click_gmail()
maximize_chrome()
click_gmail(3)


def find_url_bar(tab_count=1):
    time.sleep(speed_frequency + 4)
    for i in range(tab_count):
        pyautogui.hotkey('Shift', 'tab')
        time.sleep(0.10)
    # pyautogui.hotkey('enter')


find_url_bar(2)


def write_twist_tv_url():
    time.sleep(speed_frequency)
    pyautogui.write('https://www.twitch.tv/', interval=0.1)
    pyautogui.hotkey('enter')


write_twist_tv_url()


def find_sign_up(tab_count=1):
    time.sleep(speed_frequency + 4)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.10)
    # pyautogui.hotkey('enter')


find_sign_up(8)

