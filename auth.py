import os
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings

app_id = os.getenv("MICROSOFT_APP_ID")
app_password = os.getenv("MICROSOFT_APP_PASSWORD")
tenant_id = os.getenv("MICROSOFT_APP_TENANT_ID")

SETTINGS = BotFrameworkAdapterSettings(app_id, app_password)
SETTINGS.oauth_scope = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
ADAPTER = BotFrameworkAdapter(SETTINGS)
