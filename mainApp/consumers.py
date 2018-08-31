from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MainConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		await self.send({
			"type": "websocket.accept",
		})
	
	async def receive(self, event):
		self.send({
			"type": "websocket.send",
			"text": event["text"],
		})