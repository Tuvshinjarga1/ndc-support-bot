import os
import logging
from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import asyncio
from auth import ADAPTER
# Лог тохиргоо
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Энгийн bot хариу буцаах
async def handle_bot_activity(turn_context: TurnContext):
    user_text = turn_context.activity.text
    await turn_context.send_activity(f"ECHO: {user_text}")

# Microsoft Bot Framework-ийн message receive endpoint
@app.route("/api/messages", methods=["POST"])
def messages():
    activity = Activity().deserialize(request.json)
    auth_header = request.headers.get("Authorization", "")

    try:
        # Flask sync route дотроос async function-г ажиллуулах
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            ADAPTER.process_activity(activity, auth_header, handle_bot_activity)
        )
        return jsonify({"status": "success"})
    except Exception as e:
        logger.error(f"Error processing activity: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Health check endpoint
@app.route("/health")
def health():
    logger.info("Health check called")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
