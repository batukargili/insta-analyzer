import configparser


class MongoConnection:

    def __init__(self, port=None, host=None, mongo_settings=None):
        self.__port = port  # mongodb port
        self.__host = host  # mongodb host
        self.__settings = mongo_settings

    def __str__(self):
        return "<< Connection: port={}, host={}, db={} >>".format(self.__port, self.__host, self.__settings)

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, url):
        config = configparser.ConfigParser()
        config.read(url)
        self.__settings = config

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = self.__settings.get(value, 'Port')

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = self.__settings.get(value, 'Host')
