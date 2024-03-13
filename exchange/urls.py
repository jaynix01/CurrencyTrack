from django.urls import path
from exchange import views

urlpatterns = [
    path('',views.exchange, name='exchange')
]
