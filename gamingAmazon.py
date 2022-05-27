import pyautogui
import time

speed_frequency = 2


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


print(input("press enter to start:"))
time.sleep(8)


def write_twist_tv_url():
    time.sleep(speed_frequency)
    pyautogui.write('https://gaming.amazon.com/intro', interval=0.1)
    pyautogui.hotkey('enter')


write_twist_tv_url()


def new_amazon_account():
    # find_screen_pointer()
    open_browser_move_x = 1667
    open_browser_move_y = 184
    pyautogui.moveTo(open_browser_move_x, open_browser_move_y)
    time.sleep(speed_frequency)
    pyautogui.click()


new_amazon_account()
