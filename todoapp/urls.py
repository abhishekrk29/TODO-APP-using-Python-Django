from django.contrib import admin
from django.urls import path
from todoapp.views.login import Login,Logout
from todoapp.views.signup import Signup
from todoapp.views.index import index,mytodo,add_todo,delete_todo,change_todo


urlpatterns = [    
    path('',index,name='homepage'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout,name='logout'),
    path('signup/',Signup.as_view(),name='signup'),
    path('mytodo/',mytodo,name='mytodo'),
    path('add-todo/' , add_todo,name='addtodo' ), 
    path('delete-todo/<int:id>' , delete_todo,name='deletetodo' ), 
    path('change-status/<int:id>/<str:status>' , change_todo,name='changetodo' ), 
   
]