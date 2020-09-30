from selenium.webdriver.common.keys import Keys
import time
from Models.instagram_login import InstagramSession
from Handlers.connection_handler import connection_handler


def sign_in():
    connection = connection_handler()
    session = InstagramSession(browser=connection.driver, name=connection.user_name, email=connection.email,
                               password=connection.password)
    session.browser.get(connection.settings.get('URL', 'TargetUrl'))
    time.sleep(1)
    email_input = session.browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input')
    time.sleep(1)
    password_input = session.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input')
    time.sleep(1)
    email_input.send_keys(session.name)
    time.sleep(1)
    password_input.send_keys(session.password)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(50)
