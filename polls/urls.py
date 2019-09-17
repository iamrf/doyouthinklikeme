from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('edit-form-<int:id>/', views.edit_form, name='edit-form'),
    path('form-<int:id>/edit/', views.edit_form_page, name='edit-form-page'),
    path('delete-form-<int:id>/', views.delete_form, name='delete-form'),
    path('form-management/', views.form_management, name='form-management'),
    path('user/<str:user>/', views.user_poll, name='user-poll'),
    path('tags/', views.tags, name='tags'),
    path('tag/<slug:slug>/', views.tag, name='tag'),
    path('addq/', views.add_q, name="add_q"),
    path('add-a-form/', views.add_q_page, name='add_q_page'),
    path('comment-<int:id>/', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_pass, name='change_pass'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='login'),
    path('user-signing/', views.user_signing, name="user-signing"),
    path('pvote/<int:id>/', views.pvote, name='pvote'),
    path('nvote/<int:id>/', views.nvote, name='nvote'),
    path('form-<int:id>/', views.q_page, name='q_page'),
    path('index/', views.index, name='index'),
    path('', views.intro, name='intro'),
]
