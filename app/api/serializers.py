from rest_framework import serializers

from items.models import Item
from PIL import Image


class ImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField(read_only=True)
    formats = serializers.SerializerMethodField(read_only=True)


    def get_path(self, obj):
        return obj.path.split('.')[0]
    
    def get_formats(self, obj):
        formats = []
        image = Image.open(obj.path)
        if image.format.lower() == obj.path.split('.')[-1]:
            formats.append(image.format.lower())
        elif image.format.lower() == 'jpeg' or image.format.lower() == 'png':
            formats.append(image.format.lower())
            formats.append(obj.path.split('.')[-1])
        else:
            formats.append(image.format.lower())
        return formats

    class Meta:
        fields = ('path', 'formats')
        model = Item
    



class ItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        fields = ('name', 'number', 'price', 'status', 'image')
        model = Item

    
