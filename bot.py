import os
import sys
import traceback

from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.schema import Activity, ActivityTypes

from config import Config

config = Config()

# Create adapter
adapter_settings = BotFrameworkAdapterSettings(
    app_id=config.APP_ID,
    app_password=config.APP_PASSWORD
)
adapter = BotFrameworkAdapter(adapter_settings)

# Error handler
async def on_error(context: TurnContext, error: Exception):
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()
    
    # Check if it's an authentication error
    if "AADSTS700016" in str(error) or "unauthorized_client" in str(error):
        print("❌ Ботын тохиргооны алдаа: BOT_ID эсвэл BOT_PASSWORD буруу байна")
        print("📝 .env файлд зөв тохиргоог оруулна уу")
    else:
        await context.send_activity("The bot encountered an error or bug.")

adapter.on_turn_error = on_error

# Bot logic
async def on_message_activity(context: TurnContext):
    """Handle message activities - simple echo bot."""
    try:
        # Simple echo response
        user_message = context.activity.text
        echo_response = f"Echo: {user_message}"
        
        # Send echo response
        await context.send_activity(echo_response)
        print(f"📝 Хүлээн авсан: {user_message}")
        print(f"🔄 Илгээсэн: {echo_response}")
    except Exception as e:
        print(f"❌ Мессеж илгээхэд алдаа гарлаа: {e}")

async def on_members_added_activity(members_added, context: TurnContext):
    """Handle members added activities."""
    try:
        for member in members_added:
            if member.id != context.activity.recipient.id:
                await context.send_activity("Hello! I'm your echo bot. Send me a message and I'll echo it back to you!")
    except Exception as e:
        print(f"❌ Members added activity-д алдаа гарлаа: {e}")

async def on_turn(context: TurnContext):
    """Handle turn logic."""
    try:
        if context.activity.type == ActivityTypes.message:
            await on_message_activity(context)
        elif context.activity.type == ActivityTypes.conversation_update:
            if context.activity.members_added:
                await on_members_added_activity(context.activity.members_added, context)
    except Exception as e:
        print(f"❌ Turn processing-д алдаа гарлаа: {e}")