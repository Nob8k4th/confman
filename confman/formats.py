import configparser
import json
import tomllib
import yaml

def read_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def read_yaml(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

def write_yaml(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f)

def read_toml(path):
    with open(path, 'rb') as f:
        return tomllib.load(f)

def read_ini(path):
    parser = configparser.ConfigParser()
    parser.read(path, encoding='utf-8')
    return {s: dict(parser[s]) for s in parser.sections()}
