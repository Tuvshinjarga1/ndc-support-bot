# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import Activity, ActivityTypes

class TeamsConversationBot(ActivityHandler):
    def __init__(self, app_id: str, app_password: str):
        self.app_id = app_id
        self.app_password = app_password

    async def on_message_activity(self, turn_context: TurnContext):
        """Handle message activities."""
        user_text = turn_context.activity.text
        await turn_context.send_activity(f"ECHO: {user_text}")

    async def on_members_added_activity(
        self, members_added: list, turn_context: TurnContext
    ):
        """Handle members added activities."""
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Сайн байна уу! Би таны bot юм.")

    async def on_turn(self, turn_context: TurnContext):
        """Handle turn activities."""
        await super().on_turn(turn_context)
