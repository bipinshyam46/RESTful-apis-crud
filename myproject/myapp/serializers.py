from rest_framework import serializers
from .models import *

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'