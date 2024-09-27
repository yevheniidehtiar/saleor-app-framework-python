from typing import Type

from fastapi import Request
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
from starlette.routing import NoMatchFound

from saleor_app.errors import ConfigurationError


class LazyUrl(str):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"LazyUrl('{self.name}')"

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type["LazyUrl"], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        assert source is cls
        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                cls._serialize,
                info_arg=False,
                return_schema=core_schema.str_schema(),
            ),
        )

    @staticmethod
    def _validate(value: str):
        return value

    @staticmethod
    def _serialize(value):
        return str(value)

    def __call__(self, request: Request):
        self.request = request
        try:
            return self.resolve()
        except NoMatchFound:
            raise ConfigurationError(
                f"Failed to resolve a lazy URL, check if an endpoint named '{self.name}' is defined."
            )

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not (self.name == other.name)

    def resolve(self):
        return self.request.url_for(self.name)


class LazyPath(LazyUrl):
    # Your LazyPath implementation here
    def __str__(self):
        return f"LazyPath('{self.name}')"

    def resolve(self):
        return self.request.app.url_path_for(self.name)
