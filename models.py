from enum import Enum
from dataclasses import dataclass

@dataclass
class Product:
    website: str
    url: str
    id: int = None  # Default value of id is set to None

    def __eq__(self, __value: object) -> bool:
        return self.url == __value.url

class Website(str, Enum):
    MYAUTO = "myauto.ge"
    MYHOME = "myhome.ge"
    SS = "ss.ge"
