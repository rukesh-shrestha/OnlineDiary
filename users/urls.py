
from django.contrib import admin
from django.urls import path
from .views import SignUpPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignUpPage.as_view(),name='signup')
]
