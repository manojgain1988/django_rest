from rest_framework import serializers
from .models import Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','name','descriptions','price','stock','created_at',)