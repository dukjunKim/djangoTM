from django.core import serializers
from django.http import HttpResponse
from rest_framework import serializers
from .models import TmabTbKt10
from .models import TmabTbKt14


class tmabtbkt14Serializer(serializers.ModelSerializer):
    class Meta:
        model = TmabTbKt14
        fields = '__all__'


class tmabtbkt10Serializer(serializers.ModelSerializer):
    class Meta:
        model = TmabTbKt10
        fields = '__all__'
