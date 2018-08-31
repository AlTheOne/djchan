from django.urls import path
from mainApp.views import Main

urlpatterns = [
	path('', Main.as_view(), name='test'),
]