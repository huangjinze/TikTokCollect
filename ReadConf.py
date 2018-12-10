import configparser, json, os

def read_conf(filename):
    cf = configparser.ConfigParser()
    with open(filename, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config