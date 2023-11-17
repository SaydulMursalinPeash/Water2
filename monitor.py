import asyncio
import websockets
import flet as ft
import json
import asyncio
import websockets
'''
async def main():
    async with websockets.connect("ws://127.0.0.1:8000/ws/sensor/some_sensor_name/") as websocket:
        while True:
            try:
                data = await websocket.recv()
                print(f"Received message: {data}")
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed")
                break
'''

async def flet_app(page:ft.Page):
    text=ft.Text()
    await page.add_async(text)
    async with websockets.connect("wss://waterserver-vsqt.onrender.com/ws/sensor/some_sensor_name/") as websocket:
        while True:
            try:
                data = await websocket.recv()
                data=json.loads(data)
                print(data['temp'])
                text.value=data['temp']
                await page.update_async()
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed")
                break
    
ft.app(target=flet_app)



