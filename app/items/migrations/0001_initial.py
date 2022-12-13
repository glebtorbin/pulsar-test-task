# Generated by Django 3.2.16 on 2022-12-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('number', models.PositiveSmallIntegerField(unique=True, verbose_name='артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='цена')),
                ('status', models.CharField(choices=[('В НАЛИЧИИ', 'В наличии'), ('ПОД ЗАКАЗ', 'Под заказ'), ('ОЖИДАЕТСЯ ПОСТУПЛЕНИЕ', 'Ожидается поступление'), ('НЕТ В НАЛИЧИИ', 'Нет в наличии'), ('НЕ ПРОИЗВОДИТСЯ', 'Не производится')], default='НЕТ В НАЛИЧИИ', max_length=22, verbose_name='статус')),
                ('image', models.ImageField(blank=True, upload_to='img/', verbose_name='Картинка')),
            ],
        ),
    ]
