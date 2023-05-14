from django.urls import path
from . import views
urlpatterns = [
path('form/', views.my_form, name='form'),
path('form1/', views.my_form1, name='form1')
]