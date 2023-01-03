from aiohttp import ClientResponseError
from dataclasses import dataclass


@dataclass(frozen=True)
class HTTPRedirectionException(ClientResponseError):
    status: int
    exception: Exception
    response: str
