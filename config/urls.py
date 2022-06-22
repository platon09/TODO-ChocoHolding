"""
config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include([
        path('', include('todo.api.urls'),)
    ])),
    path('api/docs/', include_docs_urls(
        title='Employee API documentation'
    )),
]

admin.site.site_header = _("TODO Administration")
admin.site.site_title = _("TODO Admin Portal")
admin.site.index_title = _("Welcome to TODO Portal")