"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
from http import HTTPStatus
import logging
import json

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
    try:
        # JSON өгөгдлийг унших
        data = await req.json()
        
        # Хэрэглэгчийн мессежийг авах
        user_message = data.get('message', '')
        
        # Echo хариу үүсгэх
        echo_response = {
            'text': f"Таны мессеж: {user_message}",
        }
        
        return web.json_response(echo_response, status=HTTPStatus.OK)
        
    except Exception as e:
        logging.error(f"Алдаа гарлаа: {str(e)}")
        return web.Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@routes.get("/")
async def home(req: web.Request) -> web.Response:
    return web.Response(text="Echo Bot ажиллаж байна! /api/messages endpoint-д POST хүсэлт илгээнэ үү.", content_type="text/plain")

app = web.Application(middlewares=[aiohttp_error_middleware])
app.add_routes(routes)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Echo Bot эхэллээ...")
    web.run_app(app, host="0.0.0.0", port=8080)