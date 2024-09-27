from enum import Enum
from typing import Awaitable, Callable, List, Optional

from saleor_app.schemas.core import DomainName
from saleor_app.schemas.webhook import Webhook


class SaleorEventType(str, Enum):
    ADDRESS_CREATED = "ADDRESS_CREATED"
    ADDRESS_DELETED = "ADDRESS_DELETED"
    ADDRESS_UPDATED = "ADDRESS_UPDATED"
    ANY_EVENTS = "ANY_EVENTS"
    APP_DELETED = "APP_DELETED"
    APP_INSTALLED = "APP_INSTALLED"
    APP_STATUS_CHANGED = "APP_STATUS_CHANGED"
    APP_UPDATED = "APP_UPDATED"
    ATTRIBUTE_CREATED = "ATTRIBUTE_CREATED"
    ATTRIBUTE_DELETED = "ATTRIBUTE_DELETED"
    ATTRIBUTE_UPDATED = "ATTRIBUTE_UPDATED"
    ATTRIBUTE_VALUE_CREATED = "ATTRIBUTE_VALUE_CREATED"
    ATTRIBUTE_VALUE_DELETED = "ATTRIBUTE_VALUE_DELETED"
    ATTRIBUTE_VALUE_UPDATED = "ATTRIBUTE_VALUE_UPDATED"
    CATEGORY_CREATED = "CATEGORY_CREATED"
    CATEGORY_DELETED = "CATEGORY_DELETED"
    CATEGORY_UPDATED = "CATEGORY_UPDATED"
    CHANNEL_CREATED = "CHANNEL_CREATED"
    CHANNEL_DELETED = "CHANNEL_DELETED"
    CHANNEL_STATUS_CHANGED = "CHANNEL_STATUS_CHANGED"
    CHANNEL_UPDATED = "CHANNEL_UPDATED"
    CHECKOUT_CREATED = "CHECKOUT_CREATED"
    CHECKOUT_UPDATED = "CHECKOUT_UPDATED"
    COLLECTION_CREATED = "COLLECTION_CREATED"
    COLLECTION_DELETED = "COLLECTION_DELETED"
    COLLECTION_UPDATED = "COLLECTION_UPDATED"
    CUSTOMER_CREATED = "CUSTOMER_CREATED"
    CUSTOMER_DELETED = "CUSTOMER_DELETED"
    CUSTOMER_UPDATED = "CUSTOMER_UPDATED"
    DRAFT_ORDER_CREATED = "DRAFT_ORDER_CREATED"
    DRAFT_ORDER_DELETED = "DRAFT_ORDER_DELETED"
    DRAFT_ORDER_UPDATED = "DRAFT_ORDER_UPDATED"
    FULFILLMENT_CANCELED = "FULFILLMENT_CANCELED"
    FULFILLMENT_CREATED = "FULFILLMENT_CREATED"
    GIFT_CARD_CREATED = "GIFT_CARD_CREATED"
    GIFT_CARD_DELETED = "GIFT_CARD_DELETED"
    GIFT_CARD_STATUS_CHANGED = "GIFT_CARD_STATUS_CHANGED"
    GIFT_CARD_UPDATED = "GIFT_CARD_UPDATED"
    INVOICE_DELETED = "INVOICE_DELETED"
    INVOICE_REQUESTED = "INVOICE_REQUESTED"
    INVOICE_SENT = "INVOICE_SENT"
    MENU_CREATED = "MENU_CREATED"
    MENU_DELETED = "MENU_DELETED"
    MENU_ITEM_CREATED = "MENU_ITEM_CREATED"
    MENU_ITEM_DELETED = "MENU_ITEM_DELETED"
    MENU_ITEM_UPDATED = "MENU_ITEM_UPDATED"
    MENU_UPDATED = "MENU_UPDATED"
    NOTIFY_USER = "NOTIFY_USER"
    OBSERVABILITY = "OBSERVABILITY"
    ORDER_CANCELLED = "ORDER_CANCELLED"
    ORDER_CONFIRMED = "ORDER_CONFIRMED"
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_FULFILLED = "ORDER_FULFILLED"
    ORDER_FULLY_PAID = "ORDER_FULLY_PAID"
    ORDER_UPDATED = "ORDER_UPDATED"
    PAGE_CREATED = "PAGE_CREATED"
    PAGE_DELETED = "PAGE_DELETED"
    PAGE_TYPE_CREATED = "PAGE_TYPE_CREATED"
    PAGE_TYPE_DELETED = "PAGE_TYPE_DELETED"
    PAGE_TYPE_UPDATED = "PAGE_TYPE_UPDATED"
    PAGE_UPDATED = "PAGE_UPDATED"
    PERMISSION_GROUP_CREATED = "PERMISSION_GROUP_CREATED"
    PERMISSION_GROUP_DELETED = "PERMISSION_GROUP_DELETED"
    PERMISSION_GROUP_UPDATED = "PERMISSION_GROUP_UPDATED"
    PRODUCT_CREATED = "PRODUCT_CREATED"
    PRODUCT_DELETED = "PRODUCT_DELETED"
    PRODUCT_UPDATED = "PRODUCT_UPDATED"
    PRODUCT_VARIANT_BACK_IN_STOCK = "PRODUCT_VARIANT_BACK_IN_STOCK"
    PRODUCT_VARIANT_CREATED = "PRODUCT_VARIANT_CREATED"
    PRODUCT_VARIANT_DELETED = "PRODUCT_VARIANT_DELETED"
    PRODUCT_VARIANT_OUT_OF_STOCK = "PRODUCT_VARIANT_OUT_OF_STOCK"
    PRODUCT_VARIANT_UPDATED = "PRODUCT_VARIANT_UPDATED"
    SALE_CREATED = "SALE_CREATED"
    SALE_DELETED = "SALE_DELETED"
    SALE_TOGGLE = "SALE_TOGGLE"
    SALE_UPDATED = "SALE_UPDATED"
    SHIPPING_PRICE_CREATED = "SHIPPING_PRICE_CREATED"
    SHIPPING_PRICE_DELETED = "SHIPPING_PRICE_DELETED"
    SHIPPING_PRICE_UPDATED = "SHIPPING_PRICE_UPDATED"
    SHIPPING_ZONE_CREATED = "SHIPPING_ZONE_CREATED"
    SHIPPING_ZONE_DELETED = "SHIPPING_ZONE_DELETED"
    SHIPPING_ZONE_UPDATED = "SHIPPING_ZONE_UPDATED"
    STAFF_CREATED = "STAFF_CREATED"
    STAFF_DELETED = "STAFF_DELETED"
    STAFF_UPDATED = "STAFF_UPDATED"
    TRANSACTION_ACTION_REQUEST = "TRANSACTION_ACTION_REQUEST"
    TRANSLATION_CREATED = "TRANSLATION_CREATED"
    TRANSLATION_UPDATED = "TRANSLATION_UPDATED"
    VOUCHER_CREATED = "VOUCHER_CREATED"
    VOUCHER_DELETED = "VOUCHER_DELETED"
    VOUCHER_UPDATED = "VOUCHER_UPDATED"
    WAREHOUSE_CREATED = "WAREHOUSE_CREATED"
    WAREHOUSE_DELETED = "WAREHOUSE_DELETED"
    WAREHOUSE_UPDATED = "WAREHOUSE_UPDATED"

    PAYMENT_AUTHORIZE = "PAYMENT_AUTHORIZE"
    PAYMENT_CAPTURE = "PAYMENT_CAPTURE"
    PAYMENT_CONFIRM = "PAYMENT_CONFIRM"
    PAYMENT_LIST_GATEWAYS = "PAYMENT_LIST_GATEWAYS"
    PAYMENT_PROCESS = "PAYMENT_PROCESS"
    PAYMENT_REFUND = "PAYMENT_REFUND"
    PAYMENT_VOID = "PAYMENT_VOID"
    CHECKOUT_CALCULATE_TAXES = "CHECKOUT_CALCULATE_TAXES"
    ORDER_CALCULATE_TAXES = "ORDER_CALCULATE_TAXES"
    SHIPPING_LIST_METHODS_FOR_CHECKOUT = "SHIPPING_LIST_METHODS_FOR_CHECKOUT"
    ORDER_FILTER_SHIPPING_METHODS = "ORDER_FILTER_SHIPPING_METHODS"
    CHECKOUT_FILTER_SHIPPING_METHODS = "CHECKOUT_FILTER_SHIPPING_METHODS"


WebHookHandlerSignature = Optional[Callable[[List[Webhook], DomainName], Awaitable]]
