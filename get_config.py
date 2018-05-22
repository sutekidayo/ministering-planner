import requests
import json
import os


def get_config():

    if not os.path.isfile('config.json'):
        s = requests.Session()
        r = s.get('https://tech.lds.org/mobile/ldstools/config.json')
        config = r.json()
        with open('config.json', 'w+') as config_file:
            json.dump(config, config_file)
        return config
    else:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
