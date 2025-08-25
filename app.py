"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""
from http import HTTPStatus
 

from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/api/messages")
async def on_messages(req: web.Request) -> web.Response:
    try:
        body = await req.json()
    except Exception:
        body = {}

    text = body.get("text", "")
    return web.json_response({"text": text}, status=HTTPStatus.OK)

@routes.get("/health")
async def health_check(_req: web.Request) -> web.Response:
    return web.Response(status=HTTPStatus.OK, text="ok")

app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)