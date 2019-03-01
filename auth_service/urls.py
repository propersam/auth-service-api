"""
auth_service URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from .api import router
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),    
]
