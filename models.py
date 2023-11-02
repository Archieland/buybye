from enum import Enum
from dataclasses import dataclass
import re

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
    SS = "ss"

    @staticmethod
    def detect_type_from_url(url :str):
        website = re.findall('\.(.*)\.', url)[0]
        if website in (Website.MYAUTO, Website.MYHOME, Website.SS):
            return website
        return None