from selenium.webdriver.common.keys import Keys
import time
from Models.instagram_session import InstagramSession
from Handlers.connection_handler import connection_handler


def create_session():
    connection = connection_handler()
    session = InstagramSession(browser=connection.driver, name=connection.user_name, email=connection.email,
                               password=connection.password)
    session.browser.get(connection.settings.get('URL', 'TargetUrl'))
    time.sleep(1)
    return session


def sign_in():
    session = create_session()
    email_input = session.browser.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input')
    time.sleep(1)
    password_input = session.browser.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input')
    fill_inputs(email_input, password_input, session.name, session.password)

    return session


def fill_inputs(email_input, password_input, name, password):
    """
    Filling inputs takes some time so we put sleeps between each step
    """
    time.sleep(1)
    email_input.send_keys(name)
    time.sleep(1)
    password_input.send_keys(password)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
