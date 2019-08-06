from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('vote/<int:id>/', views.vote, name='vote'),
    path('q-<int:id>/', views.q_page, name='q_page'),
    path('', views.index, name='index'),
]
