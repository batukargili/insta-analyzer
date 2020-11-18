import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Handlers.mongodb_handler import insert_value
from Utils.log import init_logger

logger = init_logger(__name__, testing_mode=False)


def get_user_followers(session, username):
    session.browser.get('https://www.instagram.com/' + username)
    following_count = int(session.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header'
                                                                '/section/ul '
                                                                '/li[3]/a/span').text)

    followersLink = session.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul'
                                                          '/li[3]/a')
    followersLink.click()
    time.sleep(2)
    followingList = session.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(followingList.find_elements_by_css_selector('li'))

    followingList.click()
    actionChain = webdriver.ActionChains(session.browser)

    while numberOfFollowersInList < following_count:
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        numberOfFollowersInList = len(followingList.find_elements_by_css_selector('li'))

    following = []
    for user in followingList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        following.append(userLink)
        if len(following) == following_count:
            break
    return following


def get_following_data(username, following_list):
    following = following_list
    for followed_user in following:
        following = followed_user.split('https://www.instagram.com/', 1)[1]
        post = {"follower": username,
                "following": following,
                "date": datetime.utcnow()}
        insert_value(post)
    logger.warning("All the values inserted successfuly")
