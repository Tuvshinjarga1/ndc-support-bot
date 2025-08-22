# Bot Framework Emulator Тохиргоо

## 1. Bot Framework Emulator суулгах

[Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator/releases)-г татаж авч суулгана.

## 2. Bot тохиргоо

### Bot URL

```
http://localhost:8080/api/messages
```

### Microsoft App ID

Таны bot-ийн App ID (Azure Portal-оос авсан)

### Microsoft App Password

Таны bot-ийн App Password (Azure Portal-оос авсан)

## 3. Authentication тохиргоо

### OAuth Endpoint

```
https://login.microsoftonline.com/common/oauth2/v2.0/token
```

### Scope

```
https://graph.microsoft.com/.default
```

## 4. Алдаа засах

Хэрэв "Invalid AppId passed on token" алдаа гарвал:

1. **Environment Variables шалгах**

   ```powershell
   python debug_env.py
   ```

2. **Bot Framework Emulator-ийн тохиргоог шалгах**

   - App ID зөв эсэх
   - App Password зөв эсэх
   - Bot URL зөв эсэх

3. **Network connectivity шалгах**

   - Bot-ийн сервер ажиллаж байгаа эсэх
   - Port 8080 нээлттэй эсэх

4. **Azure Portal-ийн тохиргоог шалгах**
   - App registration зөв үүсгэгдсэн эсэх
   - Client secret хүчинтэй эсэх
   - Redirect URI зөв тохируулагдсан эсэх
