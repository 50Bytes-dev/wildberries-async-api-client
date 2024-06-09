from typing import *

from pydantic import BaseModel, Field


class GoodStatus(BaseModel):
    """
      None model
          Статус товара:
    * `2` — товар без ошибок, цена и/или скидка обновилась
    * `3` — есть ошибки, данные не обновились


    """
