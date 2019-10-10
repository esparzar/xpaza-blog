from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^main_page$', views.main_page, name='main_page'),
	url(r'^js_page$', views.js_page, name='js_page'),
]