from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="app-home"),
	path('about', views.about, name='app-about'),
	path('/article', views.article, name="app-article"),
]