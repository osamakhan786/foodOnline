from django.urls import path

from accounts.views import registerUser
from . import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser' )
]