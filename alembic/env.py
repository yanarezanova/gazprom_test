from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from app.database import DATABASE_URL, Base
from app.models import *

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Указываем target_metadata для миграций
target_metadata = Base.metadata


def run_migrations_online():
    # Создаем подключение к базе данных
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Подключаемся к базе данных и запускаем миграции
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        # Начинаем транзакцию и выполняем миграции
        with context.begin_transaction():
            context.run_migrations()


# Запускаем миграции в онлайн-режиме
run_migrations_online()