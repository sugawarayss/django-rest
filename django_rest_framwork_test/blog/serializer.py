from rest_framework import serializers

from .models import Entry, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # APIとして出力したいフィールド名のタプル
        fields = ("id", "name", "mail")


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ("title", "body", "created_at", "status", "author")
