from unittest.mock import AsyncMock, Mock, create_autospec

import pytest

from saleor_app.app import SaleorApp
from saleor_app.schemas.handlers import SaleorEventType
from saleor_app.schemas.manifest import Extension, Manifest


@pytest.fixture
def manifest():
    return Manifest(
        name="Sample Saleor App",
        version="0.1.0",
        about="Sample Saleor App seving as an example.",
        data_privacy="",
        data_privacy_url="http://172.17.0.1:5000/dataPrivacyUrl",
        homepage_url="http://172.17.0.1:5000/homepageUrl",
        support_url="http://172.17.0.1:5000/supportUrl",
        id="saleor-simple-sample",
        permissions=["MANAGE_PRODUCTS", "MANAGE_USERS"],
        extensions=[
            Extension(
                label="Custom Product Create",
                mount="PRODUCT_OVERVIEW_CREATE",
                target="POPUP",
                permissions=["MANAGE_PRODUCTS"],
                url="/extension",
            )
        ],
    )


@pytest.fixture
def get_webhook_details():
    return AsyncMock()


async def _webhook_handler():
    pass


@pytest.fixture
def webhook_handler():
    return create_autospec(_webhook_handler)


@pytest.fixture
def saleor_app(manifest):
    saleor_app = SaleorApp(
        manifest=manifest,
        validate_domain=AsyncMock(),
        save_app_data=AsyncMock(),
        use_insecure_saleor_http=False,
        development_auth_token="test_token",
    )

    saleor_app.get("/configuration", name="configuration-form")(lambda x: x)
    saleor_app.get("/extension", name="extension")(lambda x: x)
    saleor_app.get("/test_webhook_handler", name="test-webhook-handler")(lambda x: x)
    saleor_app.include_saleor_app_routes()
    return saleor_app


@pytest.fixture
def saleor_app_with_webhooks(saleor_app, get_webhook_details, webhook_handler):
    saleor_app.include_webhook_router(get_webhook_details)
    saleor_app.webhook_router.http_event_route(SaleorEventType.PRODUCT_CREATED)(
        webhook_handler
    )
    saleor_app.webhook_router.http_event_route(SaleorEventType.PRODUCT_UPDATED)(
        webhook_handler
    )
    saleor_app.webhook_router.http_event_route(SaleorEventType.PRODUCT_DELETED)(
        webhook_handler
    )

    return saleor_app


@pytest.fixture
def mock_request(saleor_app):
    return Mock(app=saleor_app, body=AsyncMock(return_value=b"request_body"))


@pytest.fixture
def mock_request_with_metadata(saleor_app):
    return AsyncMock(
        app=saleor_app,
        json=AsyncMock(
            return_value=[
                {
                    "meta": {
                        "issued_at": "2022-03-09T14:42:00.756412+00:00",
                        "version": "3.1.0-a.25",
                        "issuing_principal": {"id": "VXNlcjox", "type": "user"},
                    }
                }
            ]
        ),
    )
