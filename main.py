import flet as ft
import asyncio


async def main(page: ft.Page):
    page.window_height = 1280
    page.window_width = 720
    page.window_resizable = False
    page.padding = 0

    botonAzul = ft.Stack(
        [ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE, border_radius=50),
         ft.Container(width=70, height=70, left=5, top=5, bgcolor=ft.colors.BLUE, border_radius=50)]
    )

    itemsSuperior = [
        ft.Container(botonAzul, width=80, height=80),
        ft.Container(width=40, height=40,
                     bgcolor=ft.colors.RED_200, border_radius=50),
        ft.Container(width=40, height=40,
                     bgcolor=ft.colors.YELLOW, border_radius=50),
        ft.Container(width=40, height=40,
                     bgcolor=ft.colors.GREEN, border_radius=50),
    ]

    itemCentral = ft.Stack([
        ft.Container(width=600, height=400, bgcolor=ft.colors.WHITE),
        ft.Container(width=550, height=350,
                     bgcolor=ft.colors.BLACK, top=25, left=25),
        ft.Image(
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/197.png", scale=10, width=50, height=50, top=350 / 2, right=550/2
        )
    ])

    itemInferior = [ft.Container(width=50, border=ft.border.all()),]

    superior = ft.Container(
        content=ft.Row(itemsSuperior),
        width=600,
        height=80,
        margin=ft.margin.only(top=40),
    )
    centro = ft.Container(content=itemCentral, width=600, height=400,
                          margin=ft.margin.only(top=40), alignment=ft.alignment.center)
    inferior = ft.Container(
        content=ft.Row(itemInferior), width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all()
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
