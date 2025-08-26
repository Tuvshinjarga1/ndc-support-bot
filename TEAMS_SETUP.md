# Microsoft Teams Bot Тохиргоо

## 🚨 Алдааны мэдээлэл

Таны бот дараах алдааг гаргаж байна:

```
AADSTS700016: Application with identifier '43da8dad-8d13-4b3f-ba03-e00aee84d03d' was not found in the directory 'Bot Framework'
```

Энэ нь Microsoft Teams ботын тохиргоо дутуу байгааг илэрхийлнэ.

## 🔧 Тохиргооны алхмууд

### 1. Azure Portal дээр бот үүсгэх

1. [Azure Portal](https://portal.azure.com) руу орно уу
2. "Azure Bot" хайж олоно уу
3. "Create" дарна уу
4. Дараах мэдээллийг оруулна уу:
   - **Bot handle**: `your-bot-name`
   - **Subscription**: Таны subscription
   - **Resource group**: Шинэ эсвэл одоо байгаа resource group
   - **Region**: Ойрхон region
   - **Pricing tier**: Free (F0)

### 2. Bot Framework тохиргоо

1. Azure Bot үүсгэсний дараа "Configuration" руу орно уу
2. Дараах мэдээллийг хуулж авна уу:
   - **Microsoft App ID**: Энэ бол таны `BOT_ID`
   - **Microsoft App Password**: Энэ бол таны `BOT_PASSWORD`

### 3. .env файл тохируулах

```env
BOT_ID=your_microsoft_app_id_here
BOT_PASSWORD=your_microsoft_app_password_here
BOT_TYPE=MultiTenant
BOT_TENANT_ID=your_tenant_id_here
```

### 4. Messaging endpoint тохируулах

1. Azure Bot-ийн "Configuration" хэсэгт
2. **Messaging endpoint** талбарт дараах URL оруулна уу:

   ```
   https://your-domain.com/api/messages
   ```

   Локал тестлэхийн тулд ngrok ашиглана уу:

   ```bash
   ngrok http 8080
   ```

### 5. Teams дээр бот нэмэх

1. [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator) татаж авна уу
2. Эсвэл Teams дээр шууд нэмнэ:
   - Teams-д орно уу
   - "Apps" хэсэгт орно уу
   - "Upload a custom app" дарна уу
   - Manifest файл оруулна уу

## 🧪 Тестлэх

### Локал тест (тохиргоогүйгээр):

```bash
python test_local.py
```

### Бүрэн тест (тохиргоотой):

```bash
python app.py
```

## 📝 Manifest файл жишээ

`manifest.json` файл үүсгэж, Teams дээр нэмнэ үү:

```json
{
  "$schema": "https://developer.microsoft.com/en-us/json-schemas/teams/v1.14/MicrosoftTeams.schema.json",
  "manifestVersion": "1.14",
  "version": "1.0.0",
  "id": "your-bot-id-here",
  "packageName": "com.example.echobot",
  "developer": {
    "name": "Your Name",
    "websiteUrl": "https://your-website.com",
    "privacyUrl": "https://your-privacy.com",
    "termsOfUseUrl": "https://your-terms.com"
  },
  "name": {
    "short": "Echo Bot",
    "full": "Simple Echo Bot for Teams"
  },
  "description": {
    "short": "A simple echo bot",
    "full": "This bot echoes back any message you send to it"
  },
  "icons": {
    "outline": "outline.png",
    "color": "color.png"
  },
  "accentColor": "#FFFFFF",
  "bots": [
    {
      "botId": "your-bot-id-here",
      "scopes": ["personal", "team", "groupchat"],
      "supportsFiles": false,
      "isNotificationOnly": false
    }
  ],
  "permissions": ["identity", "messageTeamMembers"],
  "validDomains": ["your-domain.com"]
}
```

## 🔍 Алдааг шалгах

1. **BOT_ID зөв эсэхийг шалгах**
2. **BOT_PASSWORD зөв эсэхийг шалгах**
3. **Messaging endpoint хүртээмжтэй эсэхийг шалгах**
4. **SSL сертификат зөв эсэхийг шалгах**

## 📞 Тусламж

Хэрэв асуудал үргэлжилсээр байвал:

1. Azure Bot-ийн log-уудыг шалгана уу
2. Bot Framework Emulator ашиглан тестлэнэ үү
3. ngrok ашиглан локал тестлэнэ үү
