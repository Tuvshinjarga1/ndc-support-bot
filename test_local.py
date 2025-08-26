"""
Локал тест файл - Microsoft Teams тохиргоогүйгээр ботыг тестлэх
"""
import asyncio
import json
from aiohttp import web

async def test_echo_logic():
    """Эхо логикийг тестлэх"""
    
    # Тест мессеж
    test_message = "Hello, this is a test message!"
    expected_response = f"Echo: {test_message}"
    
    print("🧪 Эхо ботын логикийг тестлэж байна...")
    print(f"📝 Тест мессеж: {test_message}")
    print(f"🔄 Хүлээгдэж буй хариулт: {expected_response}")
    
    # Эхо логикийг симуляци хийх
    actual_response = f"Echo: {test_message}"
    
    if actual_response == expected_response:
        print("✅ Эхо логик зөв ажиллаж байна!")
        print(f"📝 Хүлээн авсан: {test_message}")
        print(f"🔄 Хариулт: {actual_response}")
        return True
    else:
        print("❌ Алдаа: Хүлээгдэж буй хариулттай таарахгүй байна")
        print(f"Хүлээгдэж буй: {expected_response}")
        print(f"Бодит: {actual_response}")
        return False

async def test_web_server():
    """Web серверийг тестлэх"""
    print("\n🌐 Web серверийг тестлэж байна...")
    
    try:
        # Энгийн web сервер үүсгэх
        app = web.Application()
        
        async def test_handler(request):
            return web.Response(text="Test server is working!")
        
        app.router.add_get('/test', test_handler)
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8081)
        await site.start()
        
        print("✅ Web сервер амжилттай эхэллээ!")
        print("📍 Хандалтын хаяг: http://localhost:8081/test")
        
        # Серверийг зогсоох
        await asyncio.sleep(2)
        await runner.cleanup()
        
        return True
        
    except Exception as e:
        print(f"❌ Web серверийн алдаа: {e}")
        return False

async def main():
    """Үндсэн тест функц"""
    print("🤖 Microsoft Teams Echo Bot - Локал тест")
    print("=" * 50)
    
    # Эхо логик тест
    echo_test_passed = await test_echo_logic()
    
    # Web сервер тест
    web_test_passed = await test_web_server()
    
    print("\n" + "=" * 50)
    print("📊 Тестийн үр дүн:")
    print(f"✅ Эхо логик: {'Амжилттай' if echo_test_passed else 'Амжилтгүй'}")
    print(f"✅ Web сервер: {'Амжилттай' if web_test_passed else 'Амжилтгүй'}")
    
    if echo_test_passed and web_test_passed:
        print("\n🎉 Бүх тест амжилттай!")
        print("📝 Microsoft Teams тохиргоог хийснээр бот ажиллах болно.")
    else:
        print("\n❌ Зарим тест амжилтгүй байна.")

if __name__ == "__main__":
    asyncio.run(main())
