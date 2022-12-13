from django.db import models

from app.settings import MEDIA_URL

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
    image = models.ImageField(
        'Картинка',
        upload_to=MEDIA_URL,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.image.path.split('.')[1] == ('png' or 'jpg'):
            self.status = OUT_OF_STOCK
            super(Item, self).save(*args, **kwargs)
        super(Item, self).save(*args, **kwargs)

            


