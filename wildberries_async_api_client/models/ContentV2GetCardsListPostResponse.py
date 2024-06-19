from typing import *

from pydantic import BaseModel, Field


class ContentV2GetCardsListPostResponse(BaseModel):
    """
    None model

    """

    cards: Optional[List[Dict[str, Any]]] = Field(alias="cards", default=None)

    cursor: Optional[Dict[str, Any]] = Field(alias="cursor", default=None)


class Photo(BaseModel):
    """Photo model

    big: str URL фото 900х1200
    c246x328: str URL фото 248х328
    c516x688: str URL фото 516х688
    square: str URL фото 600x600
    tm:  str URL фото 75x100
    """
    big: Optional[str] = None
    c246x328: Optional[str] = None
    c516x688: Optional[str] = None
    square: Optional[str] = None
    tm: Optional[str] = None


class Dimension(BaseModel):
    """Dimension model
    length: int длина см
    width: int ширина см
    height: int высота см
    """
    length: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None


class Characteristic(BaseModel):
    """Characteristic model

    id: int Идентификатор характеристики
    name: str Названи характеристики
    value: str Значение характеристики

    """
    id: Optional[int] = None
    name: Optional[str] = None
    value: Union[str, int, List[str]]


class Size(BaseModel):
    """Size model

    chrtID: int Числовой идентификатор размера для данного артикула WB
    techSize: str Размер товара (А, XXL, 57 и др.)
    wbSize: str Российский размер товара
    skus: List[str] Массив SKU Баркод товара
    """
    chrtID: Optional[int] = None
    techSize: Optional[str] = None
    wbSize: Optional[str] = None
    skus: Optional[List[str]] = None


class Tag(BaseModel):
    """Tag model

    id: int Идентификатор тега
    name: str Название тега
    color: str Цвет тега
                        Доступные цвета:
                    D1CFD7 - серый
                    FEE0E0 - красный
                    ECDAFF - фиолетовый
                    E4EAFF - синий
                    DEF1DD - зеленый
                    FFECC7 - желтый

    """
    id: Optional[int] = None
    name: Optional[str] = None
    color: Optional[str] = None


class Card(BaseModel):
    """
    Card model

    nmID: int Артикул WB
    imtID: int Идентификатор КТ. Артикулы WB из одной КТ будут иметь одинаковый imtID
    nmUUID: str нутренний технический идентификатор товара
    subjectID: int Идентификатор предмета
    vendorCode: str Артикул продавца
    subjectName: str Название предмета
    brand: str Бренд
    title: str Наименование товара
    photos: List[Photo] Массив фото
    video: str URL видео
    dimensions: Dimension Габариты упаковки товара, см
    characteristics: List[Characteristic] Массив характеристик
    sizes: List[Size] Массив размеров товара
    tags: List[Tag] Массив тегов
    """

    nmID: Optional[int] = Field(alias="nmID", default=None)
    imtID: Optional[int] = Field(alias="imtID", default=None)
    nmUUID: Optional[str] = Field(alias="nmUUID", default=None)
    subjectID: Optional[int] = Field(alias="subjectID", default=None)
    vendorCode: Optional[str] = Field(alias="vendorCode", default=None)
    subjectName: Optional[str] = Field(alias="subjectName", default=None)
    brand: Optional[str] = Field(alias="brand", default=None)
    title: Optional[str] = Field(alias="title", default=None)
    photos: Optional[List[Photo]] = Field(alias="photos", default=None)
    video: Optional[str] = Field(alias="video", default=None)
    dimensions: Optional[Dimension] = Field(alias="dimensions", default=None)
    characteristics: Optional[List[Characteristic]] = Field(alias="characteristics", default=None)
    sizes: Optional[List[Size]] = Field(alias="sizes", default=None)
    tags: Optional[List[Tag]] = Field(alias="tags", default=None)
    created_at: Optional[str] = Field(alias="created_at", default=None)
    updated_at: Optional[str] = Field(alias="updated_at", default=None)
