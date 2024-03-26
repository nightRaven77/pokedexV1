import flet as ft


async def main(page: ft.Page):
    page.window_height = 1280
    page.window_width = 720
    page.window_resizable = False
    page.padding = 0

    botonAzul = ft.Stack(
        [ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE,
                      border=ft.border.all(), border_radius=50),
         ft.Container(width=70, height=70, left=5, top=5, bgcolor=ft.colors.BLUE, border_radius=50)]
    )

    itemsSuperior = [
        ft.Container(botonAzul, width=80, height=80, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
    ]

    superior = ft.Container(
        content=ft.Row(itemsSuperior),
        width=600,
        height=80,
        margin=ft.margin.only(top=40),
        border=ft.border.all(),
    )
    centro = ft.Container(
        width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all()
    )
    inferior = ft.Container(
        width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all()
    )

    col = ft.Column(spacing=0, controls=[superior, centro, inferior])

    container = ft.Container(
        col,
        width=720,
        height=1280,
        bgcolor=ft.colors.RED,
        alignment=ft.alignment.top_center,
    )
    await page.add_async(container)


ft.app(target=main)
