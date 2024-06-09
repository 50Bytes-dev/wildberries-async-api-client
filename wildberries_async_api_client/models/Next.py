from typing import *

from pydantic import BaseModel, Field


class Next(BaseModel):
    """
    None model
        Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения следующего пакета данных

    """
