# 参考
[Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
```shell
$ cd django-rest
$ pipenv --python 3.10
$ pipenv install django djangorestframework django-filter
$ pipenv install black --dev --pre
$ pipenv install isort --dev

$ source ./.venv/bin/activate

$ pipenv shell
(django-rest)$ django-admin startproject myrest
(django-rest)$ exit

$ cd myrest/

$ pipenv run python manage.py startapp blog

# Create Model classes in blog/models.py

# migration
$ pipenv run python manage.py makemigrations
$ pipenv run python manage.py migrate

#
```


superuser
```shell
name: sugawarayasushi
main: waku.pdxppxzy@gmail.com
pass: 6116
```
