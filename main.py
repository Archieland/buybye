from clients import DatabaseClient, EmailClient
from models import Product, Website
from parsers import Parser

# Initialize clients
db_client = DatabaseClient()
email_client = EmailClient()

# TODO, add these variables as cmd argument
website = Website.MYAUTO
url = ''

parser = Parser.from_website(website=website)
candidates = [] # parser.get_products(url)

products = db_client.get_products()

new_products = list(filter(lambda x: not x in products, candidates))
db_client.add_products(new_products)

email_client.send_product_info(
    products=products
)



