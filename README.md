FoodGram
=====

Описание проекта
----------
Cайт Foodgram («Продуктовый помощник») создан для начинающих кулинаров и изысканных гурманов.

Системные требования
----------
* Python 3.7+
* Works on Linux, Windows, macOS

Стек технологий
----------
* Python 3.7
* Django 2.2
* Rest API
* SQLite3

Установка проекта из репозитория
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:mixma5ter/foodgram-project-react.git

cd foodgram-project-react
```
2. Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv

source venv/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd backend

python manage.py migrate
```
5. Заполнение БД тестовыми данными:
```bash
python manage.py load_ingridients
```
6. Запустить контейнер фронтенда:
```bash
cd ../infra

docker-compose up -d
```
7. Запустить проект:
```bash
cd -

python manage.py runserver
```
