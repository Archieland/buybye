from clients import DatabaseClient, EmailClient
from models import Website
from parsers import Parser
from config import URL, SEND_EMAIL
import logging
logging.basicConfig(filename='logs.log', level=logging.DEBUG, 
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

db_client = DatabaseClient()
email_client = EmailClient()

website, url = Website.detect_type_from_url(URL)
parser = Parser.from_website(website=website)

candidates = parser.get_products(url)

products = db_client.get_products()

new_products = list(filter(lambda x: not x in products, candidates))
db_client.add_products(new_products)

if SEND_EMAIL and len(new_products):
    email_client.send_product_info(
        products=new_products
    )



