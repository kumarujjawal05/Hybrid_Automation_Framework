import os
import configparser



config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "configurations", "config.ini")
config.read(config_path)


class ReadConfig:

    def get_application_url():
        url = config.get('common_info', 'url')
        return url

    def get_username():
        username = config.get('common_info', 'username')
        return username

    def get_password():
        password = config.get('common_info', 'password')
        return password