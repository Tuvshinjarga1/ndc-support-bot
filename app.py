import os
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import logging
from flask import Flask, request, jsonify

#logging тохиргоо
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app_id = os.getenv("MICROSOFT_APP_ID")
app_password = os.getenv("MICROSOFT_APP_PASSWORD")

logger.info(f"Bot starting app id: {app_id[:10]}..." if app_id else "No App ID")

SETTINGS = BotFrameworkAdapterSettings(app_id, app_password)
ADAPTER = BotFrameworkAdapter(SETTINGS)

app = Flask(__name__)

async def handle_bot_activity(turn_context: TurnContext):
    user_text = turn_context.activity.text

    await turn_context.send_activity(f"ECHO: {user_text}")

@app.route("/api/messages", methods=["POST"])
def messages():
    activity = Activity().deserialize(request.json)
    auth_header = request.headers.get("Authorization", "")
    
    try:
        task = ADAPTER.process_activity(activity, auth_header, handle_bot_activity)
        return jsonify({"status": "success"})
    except Exception as e:
        logger.error(f"Error processing activity: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/health")
def health():
    logger.info("Health check")
    logger.info(f"App ID: {app_id[:5]}...")
    logger.info(f"App password: {app_password[:5]}...")
    return "OK"

if __name__ == "__main__":
    app.run(port=8080)