from typing import *

from pydantic import BaseModel, Field


class ResponseWithDate(List[Dict[str, Any]]):
    """
    None model
        Ответ при запросе с dates

    """
