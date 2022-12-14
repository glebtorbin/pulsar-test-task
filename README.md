## Описание проекта:
В проекте реализован REST API-сервис для доступа к базе данных с товарами.

### Через API-сервис можно сделать следующие запросы:
* Получение публикаций методом GET /api/v1/items/.  Пример ответа ниже. При указании параметров filter и search - можно отфильтровать позиции по статусу или выполнить поиск по полям name и number.
```
[
    {
        "name": "photo",
        "number": 1223321,
        "price": "12.00",
        "status": "ПОД ЗАКАЗ",
        "image": {
            "path": "/Users/glebb0/Test_tasks/pulsar-test-task/app/img/657a0ab06d2542598f2de224ce9afb3b",
            "formats": [
                "jpeg",
                "webp"
            ]
        }
    },
    {
        "name": "ty67",
        "number": 12,
        "price": "45.00",
        "status": "НЕТ В НАЛИЧИИ",
        "image": {
            "path": "/Users/glebb0/Test_tasks/pulsar-test-task/app/img/468441a139004d7c89cc312a453adcb0",
            "formats": [
                "webp"
            ]
        }
    }
```
* Получение конкретной публикации товара по id: GET /api/v1/item/<item_id>. Пример ответа ниже
```
{
        "name": "photo",
        "number": 1223321,
        "price": "12.00",
        "status": "ПОД ЗАКАЗ",
        "image": {
            "path": "/Users/glebb0/Test_tasks/pulsar-test-task/app/img/657a0ab06d2542598f2de224ce9afb3b",
            "formats": [
                "jpeg",
                "webp"
            ]
        }
    }
```

```
* Конвертер jpeg и png сделан через кастомное поле Imagefield.

```

```
* Добавить позицию можно через admin панель, предварительно создав superuser
```

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/glebtorbin/pulsar-test-task.git
```
```
cd pulsar-test-task
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
```
Создать пользователя:
```
python3 manage.py createsuperuser
```
Запустить проект:
```
python3 manage.py runserver
```
