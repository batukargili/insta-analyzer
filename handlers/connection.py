from models.connection import Connection


def connection_handler():
    connection = Connection()
    connection.settings = "conf/config.ini"
    connection.user_name = "User"
    connection.password = "User"
    connection.email = "User"
    connection.driver = connection.settings.get('SYSTEM', 'WebDriverPath')

    return connection
