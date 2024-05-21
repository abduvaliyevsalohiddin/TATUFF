from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CheckBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckBook
        fields = '__all__'
