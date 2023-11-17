import flet as ft
from flet import *

def main(page:Page):
    page.bgcolor=ft.colors.GREY_800
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    #top container
    def _expand(e):
        if e.data=="true":
            main_container.content.controls[0].height=560
            main_container.content.controls[0].update()
        else:
            main_container.content.controls[0].height=660*0.4
            main_container.content.controls[0].update()
            
         
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
                _top(),
            ]
        )
    )
    page.add(main_container)

ft.app(target=main,assets_dir='assets')

    