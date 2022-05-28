""" This script can add subscriber to prime games"""
from random import randrange
import time
import pathlib
import gspread
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")

# chrome_options.add_argument("--user-data-dir=chrome-data")
# chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("user-data-dir=chrome-data")
# chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome("Driver/chromedriver.exe", chrome_options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

credentials = Credentials.from_service_account_file(
    # 'campaign-318908-b7f2f5f17cab.json',
    'gspredforkundunce-5e3c88087406.json',
    scopes=scopes
)
gc = gspread.authorize(credentials)

# Import Groups Data Data
spreadsheet_connector = gc.open("twitch prime").worksheet('Sheet1')


# Time Counting
StartTime = time.time()
print("This Script Start " + time.ctime())

# email = "1990@gmail.com"
email = spreadsheet_connector.row_values(2)


def enter_email_password(driver, username, password):
    print("Your email :" + email, "Your password :" + password + " for gmail")
    driver.get("https://accounts.google.com/?hl=en-us")
    driver.implicitly_wait(10)
    email_xpath = "//input[@type='email']"
    driver.find_element_by_xpath(email_xpath).send_keys(username)

    # print(input("Try Manually :"))

    driver.implicitly_wait(10)
    time.sleep(4)
    next_button_xpath = "//span[contains(.,'Next')]/parent::button"
    next_button = driver.find_element_by_xpath(next_button_xpath)
    next_button.click()
    time.sleep(4)

    # print(input("Try Manually :"))

    driver.implicitly_wait(10)
    password_xpath = "//input[@type='password']"
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    driver.find_element_by_xpath(next_button_xpath).click()

    driver.implicitly_wait(10)
    driver.get("https://mail.google.com/mail/u/0/")


# enter_email_password(driver, "johnalis841@gmail.com", "globe0112358")


def twist_signup(email, password):
    print("Your email :" +email, "\nYour password :" +password + " for TwistTv account")
    driver.get("https://www.twitch.tv/")
    time.sleep(4)

    driver.find_element_by_xpath("(//button[normalize-space()='Sign Up'])[1]").click()

    time.sleep(2)
    driver.implicitly_wait(2)

    # before clicking button to open popup, store the current window handle
    main_window = driver.current_window_handle

    # Get Solution from : https://stackoverflow.com/questions/66568508/selenium-switch-to-popup-window/66568862#66568862
    # click whatever button it is to open popup

    # after opening popup, change window handle
    for handle in driver.window_handles:
        if handle != main_window:
            popup = handle
            driver.switch_to_window(popup)

    print(driver.title)  # Should now be the popup window

    username_field = driver.find_element_by_xpath("//input[@id='signup-username']")
    username_field.send_keys(str(randrange(10000000000)) + "randomusrename")

    password_field = driver.find_element_by_xpath("//input[@id='password-input']")
    password_field.send_keys(password)

    conform_password_field = driver.find_element_by_xpath("//input[@id='password-input-confirmation']")
    conform_password_field.send_keys(password)

    driver.find_element_by_xpath("//select[@aria-label='Select your birthday month']").send_keys(Keys.DOWN)

    driver.find_element_by_xpath("//input[@placeholder='Day']").send_keys("10")

    driver.find_element_by_xpath("//input[@placeholder='Year']").send_keys("1990")

    driver.find_element_by_xpath("//div[contains(text(),'Use email instead')]").click()

    driver.find_element_by_xpath("//input[@id='email-input']").send_keys(email)

    time.sleep(2)
    # action = webdriver.ActionChains(driver)
    # sign_up_button = driver.find_element_by_xpath("//div[@class='Layout-sc-nxg1ff-0 OZCSg']") # or your another selector here
    # print(sign_up_button)
    # action.move_to_element(sign_up_button)
    # action.perform()

    sign_up_button = driver.find_element_by_xpath("//div[@class='Layout-sc-nxg1ff-0 OZCSg']")
    sign_up_button.click()


def amazon_signup(email, password):
    print("Your email :" +email, "\nYour password :" +password + " for amazon original Account")
    driver.get("https://www.amazon.com/your-account")

    driver.find_element_by_xpath("//a[@id='nav-link-accountList']").click()

    driver.find_element_by_xpath("//a[@id='createAccountSubmit']").click()

    driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys("Full Name")

    driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(email)

    driver.find_element_by_xpath("//input[@id='ap_password']").send_keys(password)

    driver.find_element_by_xpath("//input[@id='ap_password_check']").send_keys(password)

    driver.find_element_by_xpath("//input[@id='continue']").click()

# print(input("Stop :"))


def amazon_gaming(email, password):
    print("Your email :" +email, "\nYour password :" +password + " for amazon gaming")
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.get("https://gaming.amazon.com/intro")
    print(input("Try Gaming Account :  "))
    driver.find_element_by_xpath("//div[@class='sign-up-button tw-pd-x-9 tw-pd-y-05']").click()

    driver.find_element_by_xpath("//button[@class='tw-interactive tw-button tw-button--full-width tw-button--large tw-button--prime']").click()

    driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(email)

    driver.find_element_by_xpath("//input[@id='ap_password']").send_keys(password)

    driver.find_element_by_xpath("//input[@id='signInSubmit']").click()


for i in range(10):
    print(f"We are working for {i} no account")
    twist_signup(email[i], email[i+1])
    print(input("Veryfi Using Gmail :  "))
    amazon_signup(email[i], email[i+1])
    print(input("Solve Puzzle and enter OTP :  "))
    amazon_gaming(email[i], email[i+1])
    print(input("Go for Second Email :"))

time.sleep(4)
