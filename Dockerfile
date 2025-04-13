# Dockerfile
FROM python:3.9-slim

# Задаём рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем исходный код
COPY . .

# Открываем порт приложения
EXPOSE 8000

# Команда для запуска приложения через uvicorn
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --no-access-log