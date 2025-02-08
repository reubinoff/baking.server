import logging
from collections.abc import Awaitable, Callable, Sequence
from functools import lru_cache

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

LOGGER = logging.getLogger(__name__)


@lru_cache
def get_middlewares() -> Sequence[Middleware] | None:
    origins = [
        "*",
    ]

    middlewares = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(BaseHTTPMiddleware, dispatch=add_security_headers),
        Middleware(BaseHTTPMiddleware, dispatch=exceptions),
        # Middleware(SentryMiddleware)
    ]

    return middlewares


async def add_security_headers(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=31536000 ; includeSubDomains"
    return response


async def exceptions(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    try:
        response = await call_next(request)
    except ValidationError as e:
        LOGGER.exception("Validation error")
        print(e.errors())
        response = JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": e.errors()},
        )
    except ValueError:
        LOGGER.exception("Value error")
        response = JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": [{"msg": "Value error", "loc": ["Unknown"], "type": "Unknown"}]},
        )

    return response
