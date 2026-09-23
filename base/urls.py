from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('wish/<int:pk>/', wish_detail, name='wish_detail'),
    path('angel/<int:pk>/', angel_detail, name='angel_detail'),
    path('category/<int:pk>/', category_wishes, name='category_wishes'),
]