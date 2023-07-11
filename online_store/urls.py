from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/buyer/', include('buyer.urls')),
    path('api/seller/', include('seller.urls')),
    path('api/admin_panel/', include('admin_panel.urls')),
    path('api/shop/', include('shop.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/accounts/', include('accounts.urls')),
]
