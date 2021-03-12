
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('destination',views.destination,name='destination'),
    path('book',views.book,name='book'),
     path('accounts/', include('accounts.urls')),
]