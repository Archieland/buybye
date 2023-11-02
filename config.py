import json
import os

CONFIG_JSON_PATH = 'config.json'

with open(CONFIG_JSON_PATH, 'r') as config_file:
    config_data = json.load(config_file)

DB_PATH = config_data.get('DB_PATH')
SENDGRID_EMAIL = config_data.get('SENDGRID_EMAIL')
EMAILS = config_data.get('EMAILS')
SENDGRID_API_KEY = config_data.get('SENDGRID_API_KEY')

URL = config_data.get("URL")