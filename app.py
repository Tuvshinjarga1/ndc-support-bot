"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
from http import HTTPStatus
import logging

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes

from config import Config
from bot import adapter, on_turn

# Validate tenant configuration when running as SingleTenant
_config = Config()
if (_config.APP_TYPE or "").lower() == "singletenant":
    if not (_config.APP_TENANTID or "").strip():
        logging.error("BOT_TENANT_ID is required for SingleTenant but is missing.")
        raise SystemExit(1)

routes = web.RouteTableDef()

@routes.post("/api/messages")
async def on_messages(req: web.Request) -> web.Response:
    """Handle incoming messages."""
    body = await req.json()
    activity = Activity().deserialize(body)
    
    auth_header = req.headers.get("Authorization", "")
    
    try:
        response = await adapter.process_activity(activity, auth_header, on_turn)
        return json_response(data=response.body, status=response.status)
    except Exception as e:
        logging.error(f"Error processing activity: {e}")
        return web.Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@routes.get("/api/health")
async def health_check(req: web.Request) -> web.Response:
    """Health check endpoint."""
    return web.Response(text="Bot is running", status=HTTPStatus.OK)

app = web.Application(middlewares=[aiohttp_error_middleware])
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)