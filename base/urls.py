from django.urls import path
from .views import *

urlpatterns = [
    path ('', homepage, name="homepage_url"),
    path ("wish/<int:pk>/", wish_detail, name="wish_url"),
    path ("angel/<int:pk>/", angel_detail, name="angel_url"),
    path ("category/<int:pk>/", category_wishes, name="category_url"),
]