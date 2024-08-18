from typing import *

from pydantic import BaseModel, Field


class BoosterStats(List[Dict[str, Any]]):
    """
    None model
        Статистика по средней позиции товара на страницах поисковой выдачи и каталога (для автоматических кампаний).

    """
