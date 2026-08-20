from django.urls import path 
from appointments import views

urlpatterns=[
    path('',views.appointment_list,name='appointment_list'),
    path('add/',views.add_appointments,name='add_appointments'),
    path('edit/<int:id>/',views.edit_appointments,name='edit_appointment'),
    path('delete/<int:id>/',views.delete_appointment,name='delete_appointment')
]