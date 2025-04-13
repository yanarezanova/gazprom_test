

```markdown
# Device Stats Collector

📊 Микросервис для сбора и анализа данных от устройств в реальном времени.

## 📌 Описание

Сервис принимает статистику от устройств, сохраняет её в базу данных и предоставляет агрегированную аналитику по устройствам и пользователям. Поддерживается фильтрация по устройству, пользователю и времени.

## 🔧 Стек технологий

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- Alembic (миграции)
- Docker / Docker Compose
- Locust (нагрузочное тестирование) 
```
## 📁 Структура проекта

```
.
├── app/
│   ├── api/                # Роуты FastAPI
│   ├── core/               # Настройки, зависимости
│   ├── db/                 # Инициализация БД, миграции
│   ├── models/             # ORM модели
│   ├── repositories/       # Логика доступа к данным
│   ├── schemas/            # Pydantic-схемы
│   ├── services/           # Бизнес-логика
│   └── main.py             # Точка входа
├── alembic/                # Миграции Alembic
├── tests/                  # Тесты
├── Dockerfile
├── docker-compose.yml
├── .env
├── create_tables.py        # Создание таблиц без Alembic
└── README.md


```
## 🚀 Запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/device-stats-service.git
cd device-stats-service
```

2. Создайте `.env` файл`:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/gazprom
```

3. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```

4. После запуска сервис будет доступен по адресу:  
   → http://localhost:8000/docs (Swagger UI)

## 🧠 API

### Сбор данных с устройства

```
POST /api/devices/{device_id}/data
```

**Body:**
```json
{
  "x": 1.1,
  "y": 2.2,
  "z": 3.3
}
```

### Анализ данных по устройству

```
GET /api/devices/{device_id}/analytics
```

**Параметры запроса:**
- `start_time` (опционально)
- `end_time` (опционально)

**Результат:**
```json
{
  "min": 0.0,
  "max": 9.8,
  "sum": 123.45,
  "count": 10,
  "median": 3.5
}
```

### Аналитика по пользователю

```
GET /api/users/{user_id}/analytics
```

## 🧪 Тестирование

### Нагрузочное тестирование с Locust

```bash
locust -f locustfile.py --host=http://localhost:8000
```

Откроется интерфейс по адресу: http://localhost:8089

## 🐳 Docker

### Основные команды

```bash
docker-compose build          # Сборка
docker-compose up             # Запуск
docker-compose down           # Остановка
```

### Миграции

```bash
docker-compose exec web alembic revision --autogenerate -m "init"
docker-compose exec web alembic upgrade head
```

### Альтернатива без Alembic

```bash
docker-compose exec web python create_tables.py
```



## 📎 Лицензия

Проект создан для выполнения тестового задания. Все права на использование принадлежат автору.
```

---

Если хочешь, я могу сразу сгенерировать и сам `docker-compose.yml`, `Dockerfile`, `.env.example` и `create_tables.py`, чтобы собрать полностью минимальный проект. Готов?