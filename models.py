from enum import Enum
from dataclasses import dataclass
from config import MYAUTO_URL, MYHOME_URL

@dataclass
class Product:
    website: str
    url: str
    id: int = None  # Default value of id is set to None

    def __eq__(self, __value: object) -> bool:
        return self.url == __value.url

class Website(str, Enum):
    MYAUTO = "myauto"
    MYHOME = "myhome"
    SS = "ss.ge"

    @staticmethod
    def detect_type_from_url(url :str):
        if Website.MYAUTO in url:
            return Website.MYAUTO, MYAUTO_URL
        elif Website.MYHOME in url:
            return Website.MYHOME, MYHOME_URL
        elif Website.SS in url:
            return Website.SS, None # TODO
        return None