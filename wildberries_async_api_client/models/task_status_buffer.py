from typing import *

from pydantic import BaseModel, Field


class TaskStatusBuffer(BaseModel):
    """
    None model
        Статус загрузки: `1` — в обработке


    """
