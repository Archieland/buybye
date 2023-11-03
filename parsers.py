from abc import abstractmethod
from models import Product, Website
from typing import List
import requests
from requests import Session
import json

class Parser:

    @classmethod
    def from_website(cls, website: Website):
        if website == Website.MYAUTO:
            return MyAutoParser()
        elif website == Website.MYHOME:
            # return MyHomeParser()
            pass
        elif website == Website.SS:
            # return SSParser()
            pass

    @abstractmethod
    def get_products(self, url) -> List[Product]:
        pass

class MyAutoParser(Parser):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }

    def get_products(self, url: str) -> List[Product]:
        with Session() as session:
            session.headers.update(self.headers)
            response = session.get(url)
        
        if response.status_code != 200:
                raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        prelink = 'https://www.myauto.ge/ka/pr/'
        items = json.loads(response.content)['data']['items']

        products = [Product(website='myauto', url=prelink + str(item['car_id'])) for item in items]


        return products
    
class MyHomeParser(Parser):

    def get_products(self, url) -> List[Product]:
        raise NotImplementedError()
    
class SSParser(Parser):

    def get_products(self, url) -> List[Product]:
        raise NotImplementedError()
