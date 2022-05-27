import pyautogui
import time

speed_frequency = 2

print(input("press enter to start:"))
time.sleep(8)


def write_twist_tv_url():
    time.sleep(speed_frequency)
    pyautogui.write('https://www.twitch.tv/', interval=0.1)
    pyautogui.hotkey('enter')


write_twist_tv_url()


def find_sign_up(tab_count=1):
    time.sleep(speed_frequency + 8)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.10)
    pyautogui.hotkey('enter')


find_sign_up(8)


def find_username_box(tab_count=1):
    time.sleep(speed_frequency)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.10)


find_sign_up(tab_count=1)


def write_username():
    time.sleep(speed_frequency)
    pyautogui.write('username', interval=0.1)


write_username()
find_sign_up(tab_count=1)


def write_twist_password():
    time.sleep(speed_frequency)
    pyautogui.write('username', interval=0.1)


write_twist_password()

find_sign_up(tab_count=2)

write_twist_password()

find_sign_up(tab_count=1)

pyautogui.hotkey('down')
pyautogui.hotkey('down')
pyautogui.hotkey('enter')


def find_day(tab_count=1):
    time.sleep(speed_frequency)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.10)


find_day(tab_count=1)


def write_day():
    time.sleep(speed_frequency)
    pyautogui.write('5', interval=0.1)


write_day()


def find_month(tab_count=1):
    time.sleep(speed_frequency)
    for i in range(tab_count):
        pyautogui.hotkey('tab')
        time.sleep(0.10)


find_month(tab_count=1)


def write_years():
    time.sleep(speed_frequency)
    pyautogui.write('1990', interval=0.1)


write_years()


