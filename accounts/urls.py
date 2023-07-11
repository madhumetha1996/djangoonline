from django.urls import path
from . import views
from .jwt_views import CustomTokenObtainPairView, CustomTokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    
]
