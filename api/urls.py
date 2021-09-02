from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('apps.users.urls'), name='users'),
    path('users/email-validation/',
         include('apps.email_validation.urls'), name="email_validation"),
    path('restaurants/', include("apps.restaurants.urls"), name='restaurants'),
    path('menus/', include("apps.menus.urls"), name='menus'),
    path('dishes/', include("apps.dishes.urls"), name='dishes'),
    path('tables/', include("apps.tables.urls"), name='tables'),

    # SOCKET IO EXPERIENCE DATA
    path('checks/', include("apps.checks.urls"), name='checks'),
    path('table-instances/', include("apps.table_instances.urls"),
         name='table_instances'),

]
