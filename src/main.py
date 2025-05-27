import flet as ft
import asyncio

async def main(page: ft.Page):
    await asyncio.sleep(1)

    page.window_height = 1024
    page.window_width = 720
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.9/zpix.ttf"
    }
    page.theme = ft.Theme(font_family="zpix")

    page.add(ft.Text("Hello, async world!"))



ft.app(target=main)