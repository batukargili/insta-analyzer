from Models.connection import Connection


def connection_handler():
    connection = Connection()
    connection.settings = "Config/config.ini"
    connection.user_name = "User"
    connection.password = "User"
    connection.driver = connection.settings.get('SYSTEM', 'WebDriverPath')

    return connection
