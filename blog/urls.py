from django.config.urls import includes, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
]