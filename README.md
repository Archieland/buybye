# Buybye

## Description

This project is designed to facilitate the tracking of new product listings on websites such as `myauto.ge` and `myhome.ge`. By employing specific filters defined in a configuration file, the system parses these websites and notifies the user via email whenever a new listing that matches their criteria is posted.

## Features

- Automated monitoring of website listings with user-defined filters.
- Email notifications leveraging SendGrid for any new listing detected.
- Configuration managed through a simple JSON file.
- SQLite database integration for storing records of listings.

## Configuration

Set up the project by creating a `config.json` file in the working directory. Use the following template, ensuring to replace placeholders with actual values:

```json
{
    "MYAUTO_URL" : "API_ENDPOINT_FOR_MYAUTO",
    "MYHOME_URL" : "API_ENDPOINT_FOR_MYHOME",

    "SENDGRID_API_KEY" : "YOUR_SENDGRID_API_KEY",
    "SENDGRID_EMAIL": "YOUR_SENDGRID_EMAIL",

    "DB_PATH": "database.db",

    "EMAILS": [
        "recipient1@example.com",
        "recipient2@example.com"
    ],
    "URL" : "URL_KEY",
    "SEND_EMAIL" : false
}
```

## Set up environment and run code
```cmd
conda create -n buybye python==3.10
pip install -r requirements.txt
python main.py
```

You can use cron to check websites in every n minute.
```
crontab -e
```
Example of the cron job, in every 10 minutes for conda environment named cheater:

*/10 * * * * /Users/user/anaconda3/envs/cheater/bin/python /Users/user/Desktop/buybye/main.py
