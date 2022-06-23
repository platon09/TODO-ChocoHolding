"""
config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),
    # to redirect TO'DO endoints
    path('api/v0/', include('todo.api.urls')),
    # to get access, refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # to refresh access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # api docs
    path('api/docs/', include_docs_urls(
        title='Employee API documentation'
    )),
]

# set header, title of site && title of index
admin.site.site_header = _("TODO Administration")
admin.site.site_title = _("TODO Admin Portal")
admin.site.index_title = _("Welcome to TODO Portal")