from typing import *

from pydantic import BaseModel, Field


class TaskStatusBuffer(int):
    """
    None model
        Статус загрузки: `1` — в обработке


    """
