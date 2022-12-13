from django.urls import path

from .views import ItemListView, item_detail

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('item/<int:item_id>/', item_detail)
]