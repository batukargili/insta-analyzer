import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_user_followers(session, username, max_follower):
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
        print(numberOfFollowersInList)

    followers = []
    for user in followersList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        print(userLink)
        followers.append(userLink)
        if len(followers) == max_follower:
            break
    return followers
