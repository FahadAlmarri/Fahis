from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import UserPasswordResetForm

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register', views.register, name="register"),
    #path('forgot', views.forgot, name="forgot"),

   
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="confirm.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(
    template_name='forgot.html',
    form_class=UserPasswordResetForm),name='reset_password'),

]




