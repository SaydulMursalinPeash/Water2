import flet as ft

def main(page:ft.Page):
    import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    topbar=ft.Container(
        bgcolor=ft.colors.YELLOW_300,
        border_radius=10,
        width=330,
        padding=10,
        content=ft.Row(
            
            controls=[
                ft.Icon(ft.icons.WATER),
                ft.Text('WatMon',weight=800)
            ]
        )
    )

    container=ft.Container(
        height=700,
        width=350,
        border_radius=10,
        bgcolor=ft.colors.LIGHT_BLUE,
        content=topbar,
        padding=10
    )
    container.alignment=ft.alignment.top_center
    
    
    page.add(container)



ft.app(target=main)