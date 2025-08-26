# Microsoft Teams Echo Bot

Энэ бол Microsoft Teams-д зориулж хийгдсэн энгийн эхо бот юм.

## 🚨 Чухал мэдээлэл

**Бот одоогоор Microsoft Teams тохиргоогүй байна!** Тохиргоог хийхийн тулд `TEAMS_SETUP.md` файлыг уншина уу.

## Онцлогууд

- Microsoft Teams-д зориулсан энгийн эхо бот
- Хэрэглэгчийн мессежийг эхо хэлбэрээр буцааж өгөх
- aiohttp болон botbuilder санууд ашигласан
- Docker дэмжлэг
- Алдааны мэдээллийг боловсруулах

## Суулгах

1. Шаардлагатай сануудыг суулгах:

```bash
pip install -r requirements.txt
```

2. `.env` файл үүсгэж, тохиргоог оруулах:

```env
BOT_ID=your_bot_id
BOT_PASSWORD=your_bot_password
BOT_TYPE=MultiTenant
```

## Ажиллуулах

### Локал тест (тохиргоогүйгээр):

```bash
python test_local.py
```

### Бүрэн ажиллуулах (тохиргоотой):

```bash
python app.py
```

## Docker ашиглан

```bash
docker build -t teams-echo-bot .
docker run -p 8080:8080 --env-file .env teams-echo-bot
```

## Тестлэх

### Энгийн логик тест:

```bash
python simple_test.py
```

### Локал тест:

```bash
python test_local.py
```

## API Endpoints

- `POST /api/messages` - Bot Framework мессежүүд
- `GET /api/health` - Эрүүл мэндийн шалгалт

## Тохиргоо

Microsoft Teams ботыг тохируулахын тулд:

1. `TEAMS_SETUP.md` файлыг уншина уу
2. Azure Portal дээр бот үүсгэнэ үү
3. Bot Framework тохиргоог хийнэ үү
4. Teams дээр бот нэмнэ үү

## Алдааг засах

Хэрэв алдаа гарвал:

1. `.env` файлд зөв тохиргоо байгаа эсэхийг шалгана уу
2. `TEAMS_SETUP.md` файлын зааврыг дагана уу
3. Локал тест хийж үзнэ үү: `python test_local.py`
