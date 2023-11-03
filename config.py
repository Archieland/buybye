import json
import os

CONFIG_JSON_PATH = 'config.json'

with open(CONFIG_JSON_PATH, 'r') as config_file:
    config_data = json.load(config_file)

DB_PATH = config_data.get('DB_PATH')
LOGS_PATH = config_data.get('LOGS_PATH')

SENDGRID_EMAIL = config_data.get('SENDGRID_EMAIL')
EMAILS = config_data.get('EMAILS')
SENDGRID_API_KEY = config_data.get('SENDGRID_API_KEY')


MYAUTO_URL = config_data.get("MYAUTO_URL")
MYHOME_URL =  config_data.get('MYHOME_URL')
URL = config_data.get(config_data.get("URL"))
SEND_EMAIL = config_data.get("SEND_EMAIL")