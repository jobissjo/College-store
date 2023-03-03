from django.urls import path
from . import  views
app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('department/<str:depart>', views.department, name='department'),
    path('detail/', views.detail, name='detail'),
    path('details/', views.details, name='details')
]