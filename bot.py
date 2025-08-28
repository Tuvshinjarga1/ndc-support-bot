import os
import sys
import json
import traceback
from dataclasses import asdict

from botbuilder.core import MemoryStorage, TurnContext
from teams import Application, ApplicationOptions, TeamsAdapter
from teams.state import TurnState

from config import Config

config = Config()

# Define storage and application
storage = MemoryStorage()
bot_app = Application[TurnState](
    ApplicationOptions(
        bot_app_id=config.APP_ID,
        storage=storage,
        adapter=TeamsAdapter(config),
    )
)

@bot_app.message("/echo")
async def on_message(context: TurnContext, state: TurnState):
    """Энгийн echo bot - хэрэглэгчийн мессежийг буцаан илгээнэ"""
    user_message = context.activity.text
    
    # Echo хариу үүсгэх
    echo_response = f"Таны мессеж: {user_message}"
    
    await context.send_activity(echo_response)

@bot_app.message("")
async def on_message_default(context: TurnContext, state: TurnState):
    """Бүх мессежид хариулах default handler"""
    user_message = context.activity.text
    
    # Echo хариу үүсгэх
    echo_response = f"Support echo: {user_message}"
    
    await context.send_activity(echo_response)

@bot_app.error
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("Bot-д алдаа гарлаа. Дахин оролдоно уу.")