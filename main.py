import flet as ft


async def main(page: ft.Page):
    page.window_height = 1280
    page.window_width = 720
    page.window_resizable = False
    page.padding = 0
    items_superior = [
        ft.Container(width=80, height=80, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
    ]
    superior = ft.Container(content=ft.Row(
        items_superior), width=600, height=80, margin=ft.margin.only(top=40), border=ft.border.all())
    centro = ft.Container(width=600, height=400, margin=ft.margin.only(
        top=40), border=ft.border.all())
    inferior = ft.Container(width=600, height=400, margin=ft.margin.only(
        top=40), border=ft.border.all())
    col = ft.Column(spacing=0, controls=[superior, centro, inferior])
    container = ft.Container(col, width=720, height=1280,
                             bgcolor=ft.colors.RED, alignment=ft.alignment.top_center)
    await page.add_async(container)
ft.app(target=main)
