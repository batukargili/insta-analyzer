import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Handlers.mongodb_handler import insert_value
from Utils.log import init_logger

logger = init_logger(__name__, testing_mode=False)


def get_user_followers(session, username, max_follower):

    """
    Needs an update!!!
    """
    session.browser.get('https://www.instagram.com/' + username)
    followersLink = session.browser.find_element_by_css_selector('ul li a')
    followersLink.click()
    time.sleep(2)
    followersList = session.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

    followersList.click()
    actionChain = webdriver.ActionChains(session.browser)
    while numberOfFollowersInList < max_follower:
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

    followers = []
    for user in followersList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        followers.append(userLink)
        if len(followers) == max_follower:
            break
    return followers


def etl_data(username,followers):
    followers = followers
    for follower in followers:
        following = follower.split("https://www.instagram.com/",1)[1]
        post = {"follower": username,
                "following": following,
                "date": datetime.utcnow()}
        insert_value(post)
    logger.warning("All the values inserted successfuly")

