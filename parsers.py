from abc import abstractmethod
from models import Product, Website
from typing import List

class Parser:

    def __init__(self, parser_type: Website) -> None:
        self.parser_type = parser_type

    @classmethod
    def from_website(cls, website: Website):
        if website == Website.MYAUTO:
            return MyAutoParser
        elif website == Website.MYHOME:
            return MyHomeParser
        elif website == Website.SS:
            return SSParser

    @abstractmethod
    def get_products(self, url) -> List[Product]:
        pass

class MyAutoParser(Parser):

    def get_products(self, url) -> List[Product]:
        raise NotImplementedError()
    
class MyHomeParser(Parser):

    def get_products(self, url) -> List[Product]:
        raise NotImplementedError()
    
class SSParser(Parser):

    def get_products(self, url) -> List[Product]:
        raise NotImplementedError()