from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('save',save,name='save'),
    path('addData',addData,name='addData'),
    path('viewData',viewData,name='viewData'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    
]
