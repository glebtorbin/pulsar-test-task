from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from items.models import Item
from .serializers import ItemSerializer, ImageSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET'])
def item_detail(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
        path = item.image.path.split('.')[0]
        serializer = ItemSerializer(item, many=False)
        return Response({'card': serializer.data})
    except Item.DoesNotExist:
        return Response(
            {'message': 'Товара с таким id не существует'},
            status=status.HTTP_404_NOT_FOUND
        )

