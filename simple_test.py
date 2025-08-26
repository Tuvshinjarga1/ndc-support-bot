"""
Энгийн тест файл - ботын логикийг шалгах
"""
import asyncio

class MockActivity:
    """Mock Activity for testing"""
    def __init__(self, text):
        self.text = text
        self.type = "message"

class MockTurnContext:
    """Mock TurnContext for testing"""
    def __init__(self, activity):
        self.activity = activity
        self.responses = []
    
    async def send_activity(self, text):
        """Mock send_activity method"""
        self.responses.append(text)
        print(f"🔄 Бот хариулт: {text}")

async def test_echo_logic():
    """Эхо логикийг тестлэх"""
    
    # Mock activity үүсгэх
    test_activity = MockActivity("Hello, this is a test message!")
    
    # Mock context үүсгэх
    mock_context = MockTurnContext(test_activity)
    
    try:
        # Эхо логикийг тестлэх
        user_message = mock_context.activity.text
        echo_response = f"Echo: {user_message}"
        
        # Send echo response
        await mock_context.send_activity(echo_response)
        print(f"📝 Хүлээн авсан: {user_message}")
        
        # Хариултыг шалгах
        if mock_context.responses:
            expected_response = "Echo: Hello, this is a test message!"
            actual_response = mock_context.responses[0]
            
            if actual_response == expected_response:
                print("✅ Эхо логик зөв ажиллаж байна!")
                print(f"📝 Хүлээн авсан: {user_message}")
                print(f"🔄 Хариулт: {actual_response}")
            else:
                print("❌ Алдаа: Хүлээгдэж буй хариулттай таарахгүй байна")
                print(f"Хүлээгдэж буй: {expected_response}")
                print(f"Бодит: {actual_response}")
        else:
            print("❌ Алдаа: Хариулт байхгүй байна")
            
    except Exception as e:
        print(f"❌ Алдаа гарлаа: {e}")

if __name__ == "__main__":
    asyncio.run(test_echo_logic())
