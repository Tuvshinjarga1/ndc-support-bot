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
    await context.send_activity("The bot encountered an error or bug.")

adapter.on_turn_error = on_error

# Bot logic
async def on_message_activity(context: TurnContext):
    """Handle message activities - simple echo bot."""
    # Simple echo response
    user_message = context.activity.text
    echo_response = f"Echo: {user_message}"
    
    # Send echo response
    await context.send_activity(echo_response)
    print(f"📝 Хүлээн авсан: {user_message}")
    print(f"🔄 Илгээсэн: {echo_response}")

async def on_members_added_activity(members_added, context: TurnContext):
    """Handle members added activities."""
    for member in members_added:
        if member.id != context.activity.recipient.id:
            await context.send_activity("Hello! I'm your echo bot. Send me a message and I'll echo it back to you!")

async def on_turn(context: TurnContext):
    """Handle turn logic."""
    if context.activity.type == ActivityTypes.message:
        await on_message_activity(context)
    elif context.activity.type == ActivityTypes.conversation_update:
        if context.activity.members_added:
            await on_members_added_activity(context.activity.members_added, context)