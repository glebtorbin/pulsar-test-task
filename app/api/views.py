from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from items.models import Item
from .serializers import ItemSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['number', 'name', ]
    filterset_fields = ('status', )

@api_view(['GET'])
def item_detail(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
        serializer = ItemSerializer(item, many=False)
        return Response({'card': serializer.data})
    except Item.DoesNotExist:
        return Response(
            {'message': 'Товара с таким id не существует'},
            status=status.HTTP_404_NOT_FOUND
        )

