from clients import DatabaseClient, EmailClient
from models import Website
from parsers import Parser
from config import URL, SEND_EMAIL

db_client = DatabaseClient()
email_client = EmailClient()

website, url = Website.detect_type_from_url(URL)
parser = Parser.from_website(website=website)

candidates = parser.get_products(url)

products = db_client.get_products()

new_products = list(filter(lambda x: not x in products, candidates))
db_client.add_products(new_products)

if SEND_EMAIL:
    email_client.send_product_info(
        products=new_products
    )



