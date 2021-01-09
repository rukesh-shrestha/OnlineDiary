
from django.contrib import admin
from django.urls import path
from .views import DairyPage,DairyUpdate,DairyDelete,DairyDetail,CreatePage

urlpatterns = [
    path('create/',CreatePage.as_view(),name='create'),
    path('<int:pk>/edit/',DairyUpdate.as_view(),name='update'),
    path('<int:pk>/delete/',DairyDelete.as_view(),name='delete'),
    path('<int:pk>/',DairyDetail.as_view(),name='detail'),
    path('',DairyPage.as_view(),name='dairy'),
    path('admin/', admin.site.urls),
   
]
