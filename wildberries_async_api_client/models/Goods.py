from typing import *

from pydantic import BaseModel, Field


class Goods(BaseModel):
    """
        None model
            Товары, цены и скидки для них. Максимум 1 000 товаров. Цена и скидка не могут быть пустыми одновременно.
    &lt;br&gt;&lt;br&gt;
    Если новая цена со скидкой будет хотя бы в 3 раза меньше старой, она попадёт [в карантин](https://seller.wildberries.ru/discount-and-prices/quarantine) и товар будет продаваться по старой цене. Ошибка об этом будет в ответах методов [Состояния загрузок](./#tag/Sostoyaniya-zagruzok)
    &lt;br&gt;&lt;br&gt;
    Вы можете изменить цену или скидку с помощью API либо вывести товар из карантина [в личном кабинете](https://seller.wildberries.ru/discount-and-prices/quarantine)


    """
