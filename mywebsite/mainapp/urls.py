from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list', views.dbList, name="db-list"),
    path('report/<int:reportID>', views.report, name="report"),
    path('login', views.login, name='login'),
    path('history', views.history, name='history'),
    path('register', views.register, name='register'),
    path('forgot', views.forgot, name='forgot'),
]

