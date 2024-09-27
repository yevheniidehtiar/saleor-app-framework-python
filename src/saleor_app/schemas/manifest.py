from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseModel, ConfigDict, Field

from saleor_app.schemas.utils import LazyPath, LazyUrl


class TargetType(str, Enum):
    POPUP = "POPUP"
    APP_PAGE = "APP_PAGE"


class MountType(str, Enum):
    CUSTOMER_DETAILS_MORE_ACTIONS = "CUSTOMER_DETAILS_MORE_ACTIONS"
    CUSTOMER_OVERVIEW_CREATE = "CUSTOMER_OVERVIEW_CREATE"
    CUSTOMER_OVERVIEW_MORE_ACTIONS = "CUSTOMER_OVERVIEW_MORE_ACTIONS"

    NAVIGATION_CATALOG = "NAVIGATION_CATALOG"
    NAVIGATION_CUSTOMERS = "NAVIGATION_CUSTOMERS"
    NAVIGATION_DISCOUNTS = "NAVIGATION_DISCOUNTS"
    NAVIGATION_ORDERS = "NAVIGATION_ORDERS"
    NAVIGATION_PAGES = "NAVIGATION_PAGES"
    NAVIGATION_TRANSLATIONS = "NAVIGATION_TRANSLATIONS"

    ORDER_DETAILS_MORE_ACTIONS = "ORDER_DETAILS_MORE_ACTIONS"
    ORDER_OVERVIEW_CREATE = "ORDER_OVERVIEW_CREATE"
    ORDER_OVERVIEW_MORE_ACTIONS = "ORDER_OVERVIEW_MORE_ACTIONS"

    PRODUCT_DETAILS_MORE_ACTIONS = "PRODUCT_DETAILS_MORE_ACTIONS"
    PRODUCT_OVERVIEW_CREATE = "PRODUCT_OVERVIEW_CREATE"
    PRODUCT_OVERVIEW_MORE_ACTIONS = "PRODUCT_OVERVIEW_MORE_ACTIONS"


class Extension(BaseModel):
    label: str
    mount: MountType
    target: TargetType
    permissions: List[str]
    url: Union[AnyHttpUrl, LazyUrl, LazyPath]
    model_config = ConfigDict(populate_by_name=True)


class Manifest(BaseModel):
    id: str
    permissions: List[str]
    name: str
    version: str
    about: str
    extensions: List[Extension]
    data_privacy: str = Field(..., alias="dataPrivacy")
    data_privacy_url: Union[AnyHttpUrl, LazyUrl] = Field(..., alias="dataPrivacyUrl")
    homepage_url: Union[AnyHttpUrl, LazyUrl] = Field(..., alias="homepageUrl")
    support_url: Union[AnyHttpUrl, LazyUrl] = Field(..., alias="supportUrl")
    configuration_url: Optional[Union[AnyHttpUrl, LazyUrl]] = Field(
        None, alias="configurationUrl"
    )
    app_url: Union[AnyHttpUrl, LazyUrl] = Field(
        LazyUrl("configuration-form"), alias="appUrl"
    )
    token_target_url: Union[AnyHttpUrl, LazyUrl] = Field(
        LazyUrl("app-install"), alias="tokenTargetUrl"
    )
    model_config = ConfigDict(populate_by_name=True)
