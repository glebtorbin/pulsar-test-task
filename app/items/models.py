import uuid
from django.db import models

from .fields import PhotoField


IN_STOCK = 'В НАЛИЧИИ'
UNDER_THE_ORDER = 'ПОД ЗАКАЗ'
EXPECTED_RECEIPT = 'ОЖИДАЕТСЯ ПОСТУПЛЕНИЕ'
OUT_OF_STOCK = 'НЕТ В НАЛИЧИИ'
NOT_PRODUCTED = 'НЕ ПРОИЗВОДИТСЯ'

ITEM_STATUSES = (
    (IN_STOCK, 'В наличии'),
    (UNDER_THE_ORDER, 'Под заказ'),
    (EXPECTED_RECEIPT, 'Ожидается поступление'),
    (OUT_OF_STOCK, 'Нет в наличии'),
    (NOT_PRODUCTED, 'Не производится')
)

def image_folder(instance, filename):
    return 'img/{}.webp'.format(uuid.uuid4().hex)

class Item(models.Model):
    name = models.CharField('название', max_length=200)
    number = models.PositiveIntegerField(
        'артикул', unique=True
    )
    price = models.DecimalField(
        'цена', max_digits=5, decimal_places=2
    )
    status = models.CharField(
        'статус', max_length=22,
        choices=ITEM_STATUSES,
        default=OUT_OF_STOCK
    )
    image = PhotoField(
        'Картинка',
        upload_to=image_folder,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.name
