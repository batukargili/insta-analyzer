from selenium import  webdriver
import configparser
import Config.set


config = configparser.ConfigParser()

config.read('Config/config.ini')

config.sections()

def base_conenction(config):
    """
    param: settings
    open a copy of the web browser and manipulate it directly from the Python environment.
    output: driver connection
    """

    driver = webdriver.Chrome(config.webdriver)
    driver.get(config.base_url)

def test(config):

    print(config['url']['base_url'])



test(config)
