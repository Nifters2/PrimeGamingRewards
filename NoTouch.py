"""
Library Documentation : https://pyautogui.readthedocs.io/en/latest/index.html ,
"""

import pyautogui
import time
import random
import pyperclip
from playsound import playsound


screen_size = pyautogui.size()
print(screen_size)

speed_frequency = 4
gmail_link = "aislamspondon@gmail.com"
# pyautogui.typewrite(f'{gmail_link}\n', interval=.001)
# print(input("press enter to start:"))
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

open_browser_move_x = 1873
open_browser_move_y = 739
open_browser_move = pyautogui.moveTo(open_browser_move_x, open_browser_move_y)
time.sleep(speed_frequency)
pyautogui.click()
time.sleep(speed_frequency)
pyautogui.hotkey('ctrl', 'Shift', 'M')

time.sleep(speed_frequency)
for i in range(9):
    pyautogui.hotkey('tab')
    time.sleep(0.25)

pyautogui.hotkey('Enter')
time.sleep(1)
pyautogui.hotkey('tab')
pyautogui.hotkey('Enter')
time.sleep(3)


print(input("Select Profile:"))

open_profile_move_x = 691
open_profile_move_y = 606
open_profile_move = pyautogui.moveTo(open_profile_move_x, open_profile_move_y)
time.sleep(speed_frequency)
pyautogui.click()



# print(input("Maximize:"))



