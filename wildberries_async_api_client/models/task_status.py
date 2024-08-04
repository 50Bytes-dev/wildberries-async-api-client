from typing import *

from pydantic import BaseModel, Field


class TaskStatus(BaseModel):
    """
      None model
          Статус загрузки:
    * `3` — обработана, в товарах нет ошибок, цены и скидки обновились
    * `4` — отменена
    * `5` — обработана, но в товарах есть ошибки. Для товаров без ошибок цены и скидки обновились, а ошибки в остальных товарах можно получить с помощью метода [Детализация обработанной загрузки](#tag/Istoriya-zagruzok/paths/~1api~1v2~1history~1goods~1task/get)
    * `6` — обработана, но во всех товарах есть ошибки. Их тоже можно получить с помощью метода [Детализация обработанной загрузки](#tag/Istoriya-zagruzok/paths/~1api~1v2~1history~1goods~1task/get)


    """
