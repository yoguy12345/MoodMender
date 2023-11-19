from django.urls import path
from .views import item_list
from .views import webcam_view
urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('webcam/', webcam_view, name='webcam_view'),
]
