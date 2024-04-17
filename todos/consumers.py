import json

from channels.generic.websocket import AsyncWebsocketConsumer


class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get("user")
        if self.user and self.user.is_authenticated:
            self.group_name = str(self.user.id)
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def recieve_todo(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))