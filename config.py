# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv

# Environment variable-уудыг уншиж авах
load_dotenv()

class DefaultConfig:
    """ Bot Configuration """

    PORT = int(os.getenv("PORT", 8080))
    APP_ID = os.getenv("MICROSOFT_APP_ID", "")
    APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "")
    
    def __init__(self):
        # Хэрэв environment variable-ууд тохируулагдаагүй бол warning өгөх
        if not self.APP_ID:
            print("Warning: MICROSOFT_APP_ID environment variable is not set")
        if not self.APP_PASSWORD:
            print("Warning: MICROSOFT_APP_PASSWORD environment variable is not set")
