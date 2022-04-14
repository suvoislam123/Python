from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addbook/',views.addbook, name='addbook'),
    path('addbook/addrecord/',views.addrecord, name='addrecord'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecord/',views.updaterecord, name='updaterecord'),

]