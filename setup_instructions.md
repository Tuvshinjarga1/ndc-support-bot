# Bot Framework Environment Variables Тохиргоо

## 1. Environment Variables тохируулах

### Windows PowerShell-д:

```powershell
$env:MICROSOFT_APP_ID = "таны_бодит_app_id"
$env:MICROSOFT_APP_PASSWORD = "таны_бодит_app_password"
```

### Эсвэл .env файл үүсгэж:

```env
MICROSOFT_APP_ID=таны_бодит_app_id
MICROSOFT_APP_PASSWORD=таны_бодит_app_password
```

## 2. Microsoft Bot Framework App Registration

1. [Azure Portal](https://portal.azure.com)-д орж
2. "App registrations" хэсэгт очно
3. "New registration" дарж шинэ app үүсгэнэ
4. App-ийн нэр, redirect URI тохируулна
5. "Certificates & secrets" хэсэгт "New client secret" үүсгэнэ
6. "Overview" хэсгээс Application (client) ID болон Directory (tenant) ID-г хуулж авна

## 3. Bot Framework Emulator тохиргоо

- **Bot URL**: `http://localhost:8080/api/messages`
- **Microsoft App ID**: таны bot-ийн App ID
- **Microsoft App Password**: таны bot-ийн App Password

## 4. Dependencies суулгах

```bash
pip install -r requirements.txt
```

## 5. Bot ажиллуулах

```bash
python app.py
```

## 6. Алдаа засах

Хэрэв "Invalid AppId passed on token" алдаа гарвал:

1. Environment variable-ууд зөв тохируулагдсан эсэхийг шалгана
2. Microsoft App ID болон App Password зөв эсэхийг шалгана
3. Bot Framework Emulator-ийн тохиргоог шалгана
4. Network connectivity-г шалгана

## 7. Шинэчлэлтүүд

- Flask-аас aiohttp руу шилжсэн
- Microsoft-ийн албан ёсны жишээ кодыг ашигласан
- Илүү сайн error handling нэмсэн
- Authentication-г илүү сайн удирдсан
