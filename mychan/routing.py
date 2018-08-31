from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer
from mainApp.consumers import MainConsumer


application = ProtocolTypeRouter({
	#Empty, HTTP - default
	'websocket': AuthMiddlewareStack(
		URLRouter([
			path('ws/chat/<str:room_name>/', ChatConsumer),
			path('ws/testing/', MainConsumer),
		])
	)
}) 