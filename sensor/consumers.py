import django
django.setup()
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import datetime
from asgiref.sync import sync_to_async,async_to_sync
from django.core.exceptions import ObjectDoesNotExist
import base64 as base
from django.core.files.base import ContentFile
import binascii
from PIL import Image
import io
from .models import SenosrInstance
class Sensor(AsyncWebsocketConsumer):
    async def connect(self):
        print('entered------------------------------------')
        self.sensor_name=self.scope['url_route']['kwargs']['sensor_name']
        self.room_name = self.sensor_name
        name = self.room_name
        self.room_group_name = f'sensor_{name}'
        print('---------------------------------------------')
        
        if self.room_name=='' or self.room_name==None:
            await self.close()
        try:
            self.sensor_instance=await sync_to_async(SenosrInstance.objects.get)(name=self.room_name)
        except ObjectDoesNotExist as e:
            self.sensor_instance=await sync_to_async(SenosrInstance.objects.create)(name=self.room_name)
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print('Disconnected')
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            print(text_data)
            text_data_json = json.loads(text_data)
            temp = text_data_json['temp']
            tds=text_data_json['tds']
            do=text_data_json['do']
            cond=text_data_json['cond']
        except (json.JSONDecodeError, KeyError):
            print('error')
            return

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'chat_room':{'name':self.room_name},
                'temp': temp,
                'tds':tds,
                'do':do,
                'cond':cond,
                'time':str(datetime.datetime.now()),
                
            }
        )

    async def chat_message(self, event):
        message = event

        # Send message to WebSocket
        print(message)
        await self.send(text_data=json.dumps(message))