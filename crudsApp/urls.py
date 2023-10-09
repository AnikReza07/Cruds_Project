from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('delete/<int:id>/', delete, name = 'delete'),
    path('create/', create, name = 'create'),
    path('login_page/', login_page, name ='login_page'),
    path('single_prof/<int:id>/', single_prof, name='single_prof'),
    path('update_prof/<int:id>/', update_prof, name='update_prof'),

]