from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_car, name='add_car'),
    path('edit/<int:id>',views.edit_car, name='edit_car'),
    path('delte/<int:id>',views.delete_car, name='delete_car'),

]