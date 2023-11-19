from django.urls import path
from .views import home
from .views import webcam_view
urlpatterns = [
    path('items/', home, name='home'),
    path('webcam/', webcam_view, name='webcam_view'),
]
