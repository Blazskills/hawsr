from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path("test/", views.testaccount.as_view(), name="testme"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("login/", views.LoginView.as_view(), name="Login"),
    path("create/user/", views.CreateUserView.as_view(), name="create_user"),
    path("update/user/", views.UpdateCurrentUserView.as_view(), name="update_user"),
    path("update/any/user/<int:pk>/", views.UpdateAnyUserView.as_view(), name="update_any_user"),
    path('delete/any/user/<int:pk>/', views.DeleteAnyUserView.as_view(), name='delete_any_user'),
    path('view/any/user/<int:pk>/', views.ViewAnyUserView.as_view(), name='view_any_user'),

]
