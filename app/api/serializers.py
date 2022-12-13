from rest_framework import serializers

from items.models import Item
from app.settings import MEDIA_URL


class ImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField(read_only=True)
    formats = serializers.SerializerMethodField(read_only=True)


    def get_path(self, obj):
        return obj.path.split('.')[0]
    
    def get_formats(self, obj):
        return [obj.path.split('.')[1]]

    class Meta:
        fields = ('path', 'formats')
        model = Item
    



class ItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer()


    class Meta:
        fields = ('name', 'number', 'price', 'status', 'image')
        model = Item

    
