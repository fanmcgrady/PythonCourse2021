import configparser

class ReadConfig:
    def __init__(self, filepath='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(filepath, encoding='utf-8')

    def get_value(self, key):
        return self.config.get('email-config', key)