from django.contrib import admin
from django.urls import path, include
from reminder import views


urlpatterns = [
    path('',views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login_user, name="login_user"),
    path('logout', views.logout_user, name= "logout_user"),
    path('task', views.task, name="task"),
    path('view', views.view, name="view"),
    path('search', views.search, name="search"),
    path('delete/<int:id>', views.delete, name="delete/<int:id>"),
    path('update/<int:id>', views.update, name="update/<int:id>"),
    path('update_record/<int:id>', views.update_record, name="update_record/<int:id>"),
]
