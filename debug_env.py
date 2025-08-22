import os
from dotenv import load_dotenv

# Environment variable-уудыг уншиж авах
load_dotenv()

print("=== Environment Variables Debug ===")
print(f"MICROSOFT_APP_ID: {os.getenv('MICROSOFT_APP_ID', 'NOT SET')}")
print(f"MICROSOFT_APP_PASSWORD: {'SET' if os.getenv('MICROSOFT_APP_PASSWORD') else 'NOT SET'}")
print(f"MICROSOFT_APP_TENANT_ID: {os.getenv('MICROSOFT_APP_TENANT_ID', 'NOT SET')}")

# Auth module-ийн тохиргоог шалгах
try:
    from auth import SETTINGS
    print(f"\n=== Auth Settings ===")
    print(f"App ID: {SETTINGS.app_id}")
    print(f"App Password: {'SET' if SETTINGS.app_password else 'NOT SET'}")
    print(f"OAuth Scope: {SETTINGS.oauth_scope}")
except Exception as e:
    print(f"Auth module error: {e}")
