# 参考

[Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)

```shell
$ cd django-rest

# pipenv 仮想環境の作成
$ pipenv --python 3.10
# 仮想環境に外部ライブラリを追加
$ pipenv install django djangorestframework django-filter
# 開発で使用するコードフォーマッタを追加
$ pipenv install black --dev --pre
$ pipenv install isort --dev

# 仮想環境を有効化
$ source ./.venv/bin/activate
```

# 1. プロジェクトの作成
```shell
# 仮想環境に入る
$ pipenv shell
# プロジェクトを作成
(django-rest)$ django-admin startproject {your project name}
(django-rest)$ exit

$ cd {your project name}
# django appを作成
$ pipenv run python manage.py startapp {your app name}
```

# 2. モデルファイルを作成
## 2.1 create models in models.py
```python
# {your app name}/models.py
from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  mail = models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

## 2.2 Django管理画面に作成したモデルを表示するようにする
```python
#{your app name}/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
```

# 3. マイグレーション
## 3.1 settings.pyに作成したappを追記する。
```python
# settings.py
INSTALLED_APP = [
    #...
    "{your app name}",
]
```
## 3.2 migration実行
```shell
# make migration file
$ pipenv run python manage.py makemigrations
# migrate execution by migration file
$ pipenv run python manage.py migrate
```


## 3.3 確認
```shell
# superuserを作成
$ pipenv run python manage.py createsuperuser
#   Username (leave blank to use 'hoge'): 
#   Email address:
#   Password:
#   Password (again):
#   Superuser created successfully.
  
# ローカルのサーバを起動
$ pipenv run python manage.py runserver
```
## 3.4 管理画面にアクセスして確認
[manage page of Django](http://localhost:8000/admin)

# 4. REST framework
```python
# settings.py
INSTALLED_APPS = (
    # ...
    "rest_framework",
)
```
- REST APIを作成するには、以下の3つを定義する必要がある
  - Serializer : Modelをどのようにシリアライス(デシリアライズ)するかを決めるためのクラス
  - ViewSet : APIのクエリをどう解釈するかを決めるもの
  - URL pattern : DjangoにURLのパターンを登録するもの

## 4.1 Serializerの定義
```python
# {your app name}/serializer.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # APIとして出力したいフィールド名
        fields = ("name", "mail")
```

## 4.2 ViewSetの定義
```python
# {your app name}/views.py
import djanggo_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer

class USerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

## 4.3 url patternの定義
Model毎にrouterを使って定義していく。
```python
# {your project name}/urls.py
from django.urls import include, re_path
from django.contrib import admin

from {your app name}.urls import router as {your app name}_router

urlpatterns = [
  re_path(r"admin/", admin.site.urls)
  re_path(r"^api/", include({your app name}_router.urls)),
]
```

```python
# {your app name}/urls.py
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
```
