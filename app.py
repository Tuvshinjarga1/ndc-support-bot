"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
from http import HTTPStatus
import logging

from aiohttp import web
from botbuilder.core.integration import aiohttp_error_middleware
from config import Config

from bot import bot_app

# Validate tenant configuration when running as SingleTenant
_config = Config()
if (_config.APP_TYPE or "").lower() == "singletenant":
    if not (_config.APP_TENANTID or "").strip():
        logging.error("BOT_TENANT_ID is required for SingleTenant but is missing.")
        raise SystemExit(1)

routes = web.RouteTableDef()

@routes.post("/api/messages")
async def on_messages(req: web.Request) -> web.Response:
    res = await bot_app.process(req)
    
    if res is not None:
        return res

    return web.Response(status=HTTPStatus.OK)

app = web.Application(middlewares=[aiohttp_error_middleware])
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)