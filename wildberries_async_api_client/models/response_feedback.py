from typing import *

from pydantic import BaseModel, Field


class ResponseFeedback(List[Dict[str, Any]]):
    """
    None model
        Массив структур отзывов

    """
