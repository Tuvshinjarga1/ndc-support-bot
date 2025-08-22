import os
import logging
from flask import Flask, request, jsonify
from botbuilder.core import TurnContext
from botbuilder.schema import Activity
import asyncio
from dotenv import load_dotenv
from auth import ADAPTER

# Environment variable-уудыг уншиж авах
load_dotenv()
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
    try:
        # Request-ийн мэдээллийг лог хийх
        logger.info(f"Received request from: {request.remote_addr}")
        logger.info(f"Authorization header present: {'Authorization' in request.headers}")
        
        activity = Activity().deserialize(request.json)
        auth_header = request.headers.get("Authorization", "")
        
        # Activity-ийн мэдээллийг лог хийх
        logger.info(f"Activity type: {activity.type}")
        logger.info(f"Activity from: {activity.from_property.id if activity.from_property else 'None'}")
        logger.info(f"Activity recipient: {activity.recipient.id if activity.recipient else 'None'}")

        # Flask sync route дотроос async function-г ажиллуулах
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            ADAPTER.process_activity(activity, auth_header, handle_bot_activity)
        )
        return jsonify({"status": "success"})
    except Exception as e:
        logger.error(f"Error processing activity: {e}")
        logger.error(f"Error type: {type(e).__name__}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Health check endpoint
@app.route("/health")
def health():
    logger.info("Health check called")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
