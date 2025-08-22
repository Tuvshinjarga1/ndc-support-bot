# Microsoft Bot Framework Bot

Энэ бол Microsoft Bot Framework ашиглан хийгдсэн энгийн echo bot юм.

## Тохиргоо

### 1. Microsoft Bot Framework App Registration

1. [Azure Portal](https://portal.azure.com)-д орж, "App registrations" хэсэгт очно
2. "New registration" дарж шинэ app үүсгэнэ
3. App-ийн нэр, redirect URI тохируулна
4. "Certificates & secrets" хэсэгт "New client secret" үүсгэнэ
5. "Overview" хэсгээс Application (client) ID болон Directory (tenant) ID-г хуулж авна

### 2. Environment Variables

`.env` файл үүсгэж дараах мэдээллийг оруулна:

```env
MICROSOFT_APP_ID=your_bot_app_id_here
MICROSOFT_APP_PASSWORD=your_bot_app_password_here
MICROSOFT_APP_TENANT_ID=your_tenant_id_here
```

### 3. Bot Framework Emulator тохиргоо

Bot Framework Emulator ашиглаж байвал:

- Bot URL: `http://localhost:8080/api/messages`
- Microsoft App ID: таны bot-ийн App ID
- Microsoft App Password: таны bot-ийн App Password

## Суулгах

```bash
pip install -r requirements.txt
```

## Ажиллуулах

```bash
python app.py
```

Bot нь `http://localhost:8080` хаяг дээр ажиллана.

## Endpoints

- `POST /api/messages` - Bot-ийн үндсэн endpoint
- `GET /health` - Health check endpoint

## Алдаа засах

Хэрэв "Invalid AppId passed on token" алдаа гарвал:

1. Environment variable-ууд зөв тохируулагдсан эсэхийг шалгана
2. Microsoft App ID болон App Password зөв эсэхийг шалгана
3. Bot Framework Emulator-ийн тохиргоог шалгана
4. Network connectivity-г шалгана
