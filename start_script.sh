#!/bin/bash
# Перейти в каталог проекта
cd kernel || exit

# Активировать Python виртуальное окружение
source venv/bin/activate

# Установить PYTHONPATH
export PYTHONPATH=.

# Запускать Python скрипт
python src/main.py