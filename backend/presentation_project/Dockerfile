# Dockerfile для Django
FROM python:3.11

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте весь проект
COPY . .

# Выполните миграции
RUN python manage.py migrate

# Запустите сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]