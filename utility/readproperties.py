import os
import configparser



config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "configuration", "config.ini")
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common_info', 'url')
        return url
   