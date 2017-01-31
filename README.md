Tutorial Django

install python 3

pip install djanggo
Note : pastikan install python-pip

bikin project
  django-admin startproject tutorial_bioskop
  NOte : pastikan install python-django-common

add project ke text editor

migrate database, secara default dia pake SQLite:
  python manage.py migrate

python manage.py createsuperuser

jalankan aplikasi :
  python manage.py runserver

jalankan aplikasi di browser :
  localhost:8000
  Note : buat accsess admin localhost:8000/admin, kalo mau ganti di urls.py

bikin apps :
  python manage.py startapp movie
