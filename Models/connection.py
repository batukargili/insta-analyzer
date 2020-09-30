from selenium import webdriver
import configparser


class Connection:

    def __init__(self, user_name=None, password=None, driver=None, settings=None):
        self.__user_name = user_name  # instagram connection user
        self.__password = password  # login password
        self.__driver = driver
        self.__settings = settings

    def __str__(self):
        return "<< Connection: user_name={}, driver={}, settings={} >>".format(self.__user_name, self.__driver,
                                                                               self.__settings)

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, url):
        config = configparser.ConfigParser()
        config.read(url)
        self.__settings = config

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        name_value = self.__settings.get(value, 'UserName')
        self.__user_name = name_value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        """
        settings.get('User', 'Password')
        """
        password_value = self.__settings.get(value, 'Password')
        self.__password = password_value

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, settings):
        """
        param: settings
        open a copy of the web browser and manipulate it directly from the Python environment.
        output: driver connection
        """
        self.__driver = webdriver.Chrome(settings)
