from django.urls import path
from . import views
from .views import custom404

handler404=custom404

urlpatterns = [
    path('', views.home, name="home"),
    path('report/<int:sampleID>', views.report, name="report"),
    path('history', views.history, name='history'),
    path('api/upload', views.apiUpload, name='apiUpload'),
    path('api/result', views.apiResult, name='apiResult'),
    path('api/', views.api, name='api'),

]

