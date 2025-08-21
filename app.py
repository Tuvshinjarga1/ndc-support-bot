import os
import logging
from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity

# Лог тохиргоо
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Орчны хувьсагчуудаас App ID, Password авах
app_id = os.getenv("MICROSOFT_APP_ID")
app_password = os.getenv("MICROSOFT_APP_PASSWORD")

logger.info(f"Bot starting app id: {app_id[:10]}..." if app_id else "No App ID configured")

# Bot adapter тохиргоо
SETTINGS = BotFrameworkAdapterSettings(app_id, app_password)
ADAPTER = BotFrameworkAdapter(SETTINGS)

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
        import asyncio
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
