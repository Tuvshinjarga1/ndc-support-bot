from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity, ActivityTypes
import asyncio
import logging
import os

# Flask app үүсгэх
app = Flask(__name__)

# Bot Framework Adapter үүсгэх
SETTINGS = BotFrameworkAdapterSettings(os.getenv("MICROSOFT_APP_ID"), os.getenv("MICROSOFT_APP_PASSWORD"))
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Logging тохируулах
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/api/messages", methods=["POST"])
def process_messages():
    try:
        logger.info("Received message request")
        
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400

        body = request.get_json()
        if not body:
            return jsonify({"error": "Request body is required"}), 400

        # Activity deserialize хийх
        activity = Activity().deserialize(body)
        logger.info(f"Activity type: {activity.type}, text: {activity.text}")

        async def logic(context):
            try:
                if activity.type == ActivityTypes.message:
                    # Хэрэглэгчийн мессежийг echo хийх
                    user_text = activity.text or "No text provided"
                    await context.send_activity(f"Таны мессежийг хүлээн авлаа: {user_text}")
                    logger.info(f"Echo response sent for: {user_text}")
                else:
                    logger.info(f"Non-message activity type: {activity.type}")
                    
            except Exception as e:
                logger.error(f"Error in logic function: {str(e)}")
                await context.send_activity(f"Серверийн алдаа: {str(e)}")

        # Bot Framework Adapter ашиглаж мессежийг боловсруулах
        auth_header = request.headers.get('Authorization', '')
        asyncio.run(ADAPTER.process_activity(activity, auth_header, logic))
        
        return jsonify({"status": "success"}), 200
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Bot is running"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")