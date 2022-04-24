from configparser import ConfigParser


def api_config(filename="config.ini", section="api"):
    parser = ConfigParser()
    parser.read(filename)
    api = {}
    params = parser.items(section)
    for param in params:
        api[param[0]] = param[1]
    return api


def gmail_config(filename="config.ini", section="gmail"):
    parser = ConfigParser()
    parser.read(filename)
    gmail = {}
    params = parser.items(section)
    for param in params:
        gmail[param[0]] = param[1]
    return gmail
