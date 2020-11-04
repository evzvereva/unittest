from selene.api import *
from selenium import webdriver

browser.set_driver(webdriver=webdriver.Chrome('/home/ekaterina/Downloads/chromedriver'))
login_element = s('[name="login"]')
password_element = s('[name="login"]')
submit_element = s('[type="submit"]')
email_entrance = s('[data-statlog="notifications.mail.logout.domik.login.big"]')
login_yandex_email = 'evzvereva.python@yandex.ru'
password_yandex = 'EVZVEREVA'


def login_with(login, password):
    browser.open_url('https://passport.yandex.ru/auth/')
    login_element.set(login)
    submit_element.click()
    password_element.set(password)
    submit_element.click()
    browser.close()
    return f'{login}, {password}'


# login_with(login_yandex_email, password_yandex)
