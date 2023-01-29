from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('report/<int:reportID>', views.report, name="report"),
    path('history', views.history, name='history'),
    path('forgot', views.forgot, name='forgot'),
]

