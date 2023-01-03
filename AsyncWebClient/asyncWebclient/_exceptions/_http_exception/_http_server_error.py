from aiohttp import ClientResponseError
from dataclasses import dataclass


@dataclass(frozen=True)
class HTTPServerException(ClientResponseError):
    status: int
    exception: Exception
    response: str
