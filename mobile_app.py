import flet as ft
from flet import *
import requests

def get_sensor_data():
    url = 'https://waterserver-vsqt.onrender.com/api/sensors'
    response = requests.get(url)
    if response.status_code == 200:  
        data = response.json()
        return data['data']
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
a=get_sensor_data()
print(a)
sen_list=[]
for key in a.keys():
    sen_list.append(
        ft.Container(
            padding=10,
            content=ft.Row(
                height=80,
                width=300,
                spacing=10,
                controls=[
                    ft.Container(
                        height=70,
                        width=70,
                        border_radius=35,
                        bgcolor='white',
                        content=Text('0',text_align='center',color='black',width='w700',size=15)
                    ),
                    ft.Text('1',size=15,color='red')
                ]
                
            )
        )
    )


def main(page:Page):
    page.bgcolor=ft.colors.GREY_800
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    #top container
    def _expand(e):
        if e.data=="true":
            main_container.content.controls[0].controls[0].height=560
            main_container.content.controls[0].update()
        else:
            main_container.content.controls[0].controls[0].height=660*0.4
            main_container.content.controls[0].update()
            
    def _sensor_list():
        #sensor_list=get_sensor_data()
        
        
        sensor_div=ft.Container(
            width=300,
            height=660*0.6,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600','lightblue900']
            ),
            border_radius=35,
            content=Column(
                alignment='start',
                scroll=True,
                controls=sen_list
            )
        )
        return sensor_div    
    def _top():
        top=ft.Container(
            width=300,
            height=660*0.4,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600','lightblue900']
            ),
            border_radius=35,
            animate=animation.Animation(
                duration=350,
                curve='decelerate',
                
            ),
            on_hover=lambda e: _expand(e),
            padding=10,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text(
                                'WatMon',
                                size=20,
                                weight='w700',
                                color='white'
                                
                            )
                        ]
                    ),
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment='center',
                        spacing=15,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                    height=90,
                                    width=90,
                                    image_src='Water/assets/wd4.png',
                                    bgcolor='white',
                                    border_radius=75
                                
                                    )
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                
                                controls=[
                                    Text(
                                        "An smart realtime sensor based filtered water monitoring system.",
                                        width=150,
                                        size=15,
                                        color='white',
                                        weight='w500'
                                        

                                    )
                                ],
                                
                            )
                        ]
                    ),
                    Divider(height=8,thickness=1,color='white10'),
                    Row(
                        alignment='center',
                        controls=[
                            IconButton(icons.REFRESH,icon_size=25,icon_color='white'),
                        ]
                    ),
                    Row(
                        alignment='center',
                        controls=[
                            Text('Refresh to update sensor list',size=12,color='white')
                        ]
                    )
                ]
            )
        )
        return top
    main_container=Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                Column(
                    alignment='start',
                    controls=[
                        _top(),
                        _sensor_list()
                    ]
                )
            ]
        )
    )
    page.add(main_container)

ft.app(target=main,assets_dir='assets')

    