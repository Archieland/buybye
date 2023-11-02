import sqlite3
from models import Product

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import SENDGRID_EMAIL, SENDGRID_API_KEY, EMAILS, DB_PATH

class EmailClient:
    def __init__(self, sendgrid_api_key=SENDGRID_API_KEY):
        self.sendgrid_client = SendGridAPIClient(sendgrid_api_key)

    def send_product_info(self, products, recipient_emails=EMAILS):
        subject = "New Product ALERT"
        from_email = SENDGRID_EMAIL 

        # Create the body of the message
        body = "Here's the list of products you might be interested in:\n\n"
        for product in products:
            body += f"Website: {product.website}, URL: {product.url}\n"

        # Send an email to each recipient
        for email in recipient_emails:
            message = Mail(
                from_email=from_email,
                to_emails=email,
                subject=subject,
                plain_text_content=body
            )
            try:
                response = self.sendgrid_client.send(message)
                print(f"Email to {email} sent successfully! Status code: {response.status_code}")
            except Exception as e:
                print(f"Failed to send email to {email}: {e}")


class DatabaseClient:
    def __init__(self, db_path=DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self.create_product_table()

    def create_product_table(self):
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS products (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 website TEXT,
                                 url TEXT
                             )''')
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_product(self, product):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO products (website, url) VALUES (?, ?)', (product.website, product.url))
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"An error occurred while adding the product: {e}")
            return None
    
    def add_products(self, products):
        for product in products:
            self.add_product(product=product)


    def get_product(self, product_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
            result = cursor.fetchone()
            if result:
                return Product(id=result[0], website=result[1], url=result[2])
        except Exception as e:
            print(f"An error occurred while retrieving the product: {e}")
            return None
        
    def get_products(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT id, website, url FROM products')
            rows = cursor.fetchall()
            products = [Product(id=row[0], website=row[1], url=row[2]) for row in rows]
            return products
        except Exception as e:
            print(f"An error occurred while retrieving products: {e}")
            return []

    def update_product(self, product_id, website, url):
        try:
            cursor = self.conn.cursor()
            cursor.execute('UPDATE products SET website = ?, url = ? WHERE id = ?', (website, url, product_id))
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"An error occurred while updating the product: {e}")
            return None

    def delete_product(self, product_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"An error occurred while deleting the product: {e}")
            return None

    def __del__(self):
        self.conn.close()

