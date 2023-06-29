from django.urls import path
from . import views

urlpatterns = [
  path('tgbot/test', views.tgbot, name='tgbot'),
  path('tgbot/test/<int:id>', views.test, name='test')
]