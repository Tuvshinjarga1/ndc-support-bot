"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
from http import HTTPStatus
import logging
import os
import traceback

from aiohttp import web
from botbuilder.core.integration import aiohttp_error_middleware

from bot import bot_app

routes = web.RouteTableDef()


def _configure_logging() -> None:
    log_level_name = os.environ.get("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, log_level_name, logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    # aiohttp access log
    logging.getLogger("aiohttp.access").setLevel(level)


@web.middleware
async def error_logging_middleware(request: web.Request, handler):
    try:
        response = await handler(request)
        return response
    except Exception as exc:  # noqa: BLE001 - we want to log any exception
        logging.exception(
            "Unhandled exception during %s %s", request.method, request.path
        )
        raise

@routes.post("/api/messages")
async def on_messages(req: web.Request) -> web.Response:
    res = await bot_app.process(req)
    if res is not None:
        return res
    return web.Response(status=HTTPStatus.OK)

@routes.get("/health")
async def health_check(_req: web.Request) -> web.Response:
    return web.Response(status=HTTPStatus.OK, text="ok")

_configure_logging()

app = web.Application(middlewares=[error_logging_middleware, aiohttp_error_middleware])
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(
        app,
        host="0.0.0.0",
        port=8080,
        access_log=logging.getLogger("aiohttp.access"),
    )