```
sudo docker-compose stop
sudo docker-compose rm backend
sudo docker-compose up -d
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py load_ingridients
sudo docker-compose exec backend python manage.py collectstatic --no-input
```