"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from app01.views import Getclassroom,UserRegistrationView
# 引入rest_framework_simplejwt路由
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    # 获取Token有效期的接口
    path('api/refresh/', TokenRefreshView.as_view(), name="refresh"),
    # 获取Token的有效性
    path('api/token/verify', TokenVerifyView.as_view(), name="token_verify"),
    # 为了在DRF路由调试界面能够使用用户相关功能需要引入以下路由
    path('', include('rest_framework.urls')),
    path('Getclassroom',Getclassroom.as_view()),
    path('registry',UserRegistrationView.as_view())
]
