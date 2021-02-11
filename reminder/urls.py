from django.contrib import admin
from django.urls import path, include
from reminder import views
from django.contrib.auth import views as auth_views


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
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="forgotPassword/reset_password.html"), name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="forgotPassword/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="forgotPassword/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="forgotPassword/password_reset_complete.html"), name="password_reset_complete"),
    path('change_password', auth_views.PasswordChangeView.as_view(template_name="forgotPassword/changePassword/change_password_form.html"), name="change_password"),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name="forgotPassword/changePassword/password_change_done.html"), name="password_change_done"),
]
