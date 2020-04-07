from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cases-home'),
    path('create', views.create, name='cases-create'),
    path('update/<int:case_id>', views.update, name='cases-update'),
    path('delete/<int:case_id>', views.delete, name='cases-delete'),
]
