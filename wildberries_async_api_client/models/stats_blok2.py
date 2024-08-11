from typing import *

from pydantic import BaseModel, Field

from .daily_stats2 import DailyStats2


class StatsBlok2(BaseModel):
    """
    None model

    """

    item_id: Optional[int] = Field(alias="item_id", default=None)

    item_name: Optional[str] = Field(alias="item_name", default=None)

    category_name: Optional[str] = Field(alias="category_name", default=None)

    advert_type: Optional[int] = Field(alias="advert_type", default=None)

    place: Optional[int] = Field(alias="place", default=None)

    views: Optional[int] = Field(alias="views", default=None)

    clicks: Optional[int] = Field(alias="clicks", default=None)

    cr: Optional[float] = Field(alias="cr", default=None)

    ctr: Optional[float] = Field(alias="ctr", default=None)

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    subject_name: Optional[str] = Field(alias="subject_name", default=None)

    atbs: Optional[int] = Field(alias="atbs", default=None)

    orders: Optional[int] = Field(alias="orders", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    cpc: Optional[float] = Field(alias="cpc", default=None)

    status: Optional[int] = Field(alias="status", default=None)

    daily_stats: Optional[DailyStats2] = Field(alias="daily_stats", default=None)

    expenses: Optional[int] = Field(alias="expenses", default=None)

    cr1: Optional[float] = Field(alias="cr1", default=None)

    cr2: Optional[int] = Field(alias="cr2", default=None)
