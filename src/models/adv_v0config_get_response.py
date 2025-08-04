from typing import *

from pydantic import BaseModel, Field

from .v0get_config_categories_response import V0getConfigCategoriesResponse


class AdvV0ConfigGetResponse(BaseModel):
    """
    None model
    """

    categories: Optional[List[Optional[V0getConfigCategoriesResponse]]] = Field(alias="categories", default=None)

    config: Optional[List[Dict[str, Any]]] = Field(alias="config", default=None)
