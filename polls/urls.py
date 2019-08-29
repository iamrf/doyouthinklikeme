from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('addq/', views.add_q, name="add_q"),
    path('add_question/', views.add_q_page, name='add_q_page'),
    path('comment-<int:id>/', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_pass, name='change_pass'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='login'),
    path('user-signing/', views.user_signing, name="user-signing"),
    path('pvote/<int:id>/', views.pvote, name='pvote'),
    path('nvote/<int:id>/', views.nvote, name='nvote'),
    path('q-<int:id>/', views.q_page, name='q_page'),
    path('', views.index, name='index'),
]
