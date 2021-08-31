from django.urls import path
from .views import (
    ListCreateMenus,
    ListCreateCategories,
    RetrieveUpdateDestroyMenus,
    RetrieveUpdateDestroyCategories
)
urlpatterns = [
    path('', ListCreateMenus.as_view(), name="list-create-menus"),
    path('<str:uuid>', RetrieveUpdateDestroyMenus.as_view(), name="rud-menus"),
    path('categories/', ListCreateCategories.as_view(),
         name="list-create-categories"),
    path('categories/<str:uuid>',
         RetrieveUpdateDestroyCategories.as_view(), name="rud-categories"),
]
