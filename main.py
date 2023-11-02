from clients import DatabaseClient, EmailClient
from models import Product, Website
from parsers import Parser
from config import URL

# Initialize clients
db_client = DatabaseClient()
email_client = EmailClient()

# TODO, add these variables as cmd argument
website = Website.detect_type_from_url(URL)

parser = Parser.from_website(website=website)
candidates = [] # parser.get_products(URL)

products = db_client.get_products()

new_products = list(filter(lambda x: not x in products, candidates))
db_client.add_products(new_products)

if len(new_products) != len(products): # First time we don't want to send emails
    email_client.send_product_info(
        products=products
    )



