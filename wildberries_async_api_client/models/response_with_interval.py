from typing import *

from pydantic import BaseModel, Field


class ResponseWithInterval(List[Dict[str, Any]]):
    """
    None model
        Ответ при запросе с interval

    """
