 
from django.urls import path, include
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('history',views.history,name='history'),
    path('logout',views.logout,name='logout'),
    path('admin',views.admin,name='admin'),
    path('add',views.add,name='add'),
    path('modify',views.modify,name='modify'),
    path('show',views.show,name='show'),
    path('showbook',views.showbook,name='showbook'),
   


]