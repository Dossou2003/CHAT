
    from channels.generic.websocket import AsyncWebsocketConsumer
    from .models import Message

    class ChatConsumer(AsyncWebsocketConsumer):
        async def connect(self):
            self.group_name = self.scope['url_route']['kwargs']['room_name']
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()

        async def disconnect(self, close_code):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

        async def receive(self, text_data=None, bytes_data=None):
            text_data_json = text_data.json()
            message = text_data_json['message']
            user = self.scope['user']
            group_name = self.scope['url_route']['kwargs']['room_name']
            group = Group.objects.get(name=group_name)
            Message.objects.create(content=message, sender=user, group=group)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': user.username,
                    'group': group_name,
                }
            )

        async def chat_message(self, event):
            message = event['message']
            user = event['user']
            group = event['group']
            await self.send(text_data=f'Message from {user} in {group}: {message}')
  </boltAction