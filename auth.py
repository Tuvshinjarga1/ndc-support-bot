import os
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings

# Environment variable-уудыг шалгах
app_id = os.getenv("MICROSOFT_APP_ID")
app_password = os.getenv("MICROSOFT_APP_PASSWORD")
tenant_id = os.getenv("MICROSOFT_APP_TENANT_ID")

# Хэрэв environment variable-ууд тохируулагдаагүй бол default утгууд ашиглах
if not app_id:
    print("Warning: MICROSOFT_APP_ID environment variable is not set")
    app_id = ""

if not app_password:
    print("Warning: MICROSOFT_APP_PASSWORD environment variable is not set")
    app_password = ""

if not tenant_id:
    print("Warning: MICROSOFT_APP_TENANT_ID environment variable is not set")
    tenant_id = ""

# Bot Framework Adapter тохиргоо
SETTINGS = BotFrameworkAdapterSettings(app_id, app_password)

# OAuth scope-г зөв тохируулах
# Хэрэв tenant_id байвал түүнийг ашиглах, үгүй бол common ашиглах
if tenant_id and tenant_id.strip():
    SETTINGS.oauth_scope = f"https://login.microsoftonline.com/{tenant_id}/.default"
else:
    SETTINGS.oauth_scope = "https://login.microsoftonline.com/common/.default"

# Authentication-г идэвхжүүлэх
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Authentication error handler нэмэх
async def on_turn_error(context, error):
    print(f"Authentication error: {error}")
    await context.send_activity("Уучлаарай, алдаа гарлаа. Дахин оролдоно уу.")

ADAPTER.on_turn_error = on_turn_error
