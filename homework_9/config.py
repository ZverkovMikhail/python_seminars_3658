import json

config = {}

with open('tgbot_conf.json', 'r', encoding='utf-8') as conf:
    config = json.loads(conf.read())


def get_token():
    global config
    return config['token']

