# import flet as ft
# import asyncio
# import aiohttp
#
# pokemonActual = 0
#
#
# async def main(page: ft.Page):
#     page.window_height = 1024
#     page.window_width = 720
#     page.window_resizable = False
#     page.window_top
#     page.padding = 0
#     page.fonts = {
#         "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.9/zpix.ttf"
#     }
#     page.theme = ft.Theme(font_family="zpix")
#
#     async def stwSprite(e):
#         global pokemonActual
#
#         numero = (pokemonActual % 1025) + 1
#         if c1.value == True:
#             spritePokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{
#                 numero}.png"
#         else:
#             spritePokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{
#                 numero}.png"
#         image.src = spritePokemon
#
#         await page.update_async()
#
#     async def getPokemon(url):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 return await response.json()
#
#     async def btnGetPokemon(e: ft.ContainerTapEvent):
#         global pokemonActual
#
#         if e.control == flechaSuperior:
#             pokemonActual += 1
#         else:
#             pokemonActual -= 1
#
#         # numero = (pokemonActual % 1025) + 1
#         if (pokemonActual % 1025) <= 0:
#             numero = (pokemonActual % 1025) + 1
#         else:
#             numero = (pokemonActual % 1025)
#
#         respuesta = await getPokemon(f"https://pokeapi.co/api/v2/pokemon/{numero}")
#         datos = f"Name: {respuesta['name']}\nAbilities:"
#         for i in respuesta['abilities']:
#             abiliity = i['ability']['name']
#             if i['is_hidden']:
#                 datos += f"\n\t{abiliity} - hidden"
#             else:
#                 datos += f"\n\t{abiliity}"
#         datos += f"\nTypes: "
#
#         for i in respuesta['types']:
#             pokemonType = i['type']['name']
#             datos += f"\n\t {pokemonType}"
#
#         datos += f"\nHeight: {respuesta['height']/10} mts."
#         datos += f"\nWeight: {respuesta['weight']/10} kg."
#
#         texto.value = datos
#
#         if c1.value == True:
#             spritePokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{
#                 numero}.png"
#         else:
#             spritePokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{
#                 numero}.png"
#         image.src = spritePokemon
#
#         await page.update_async()
#
#     async def blink():
#         while True:
#             await asyncio.sleep(1)
#             parpdeo.bgcolor = ft.colors.BLUE_100
#             await page.update_async()
#             await asyncio.sleep(0.1)
#             parpdeo.bgcolor = ft.colors.BLUE
#             await page.update_async()
#
#     parpdeo = ft.Container(width=70, height=70, left=5,
#                            top=5, bgcolor=ft.colors.BLUE, border_radius=50)
#
#     botonAzul = ft.Stack(
#         [ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE, border_radius=50),
#          parpdeo
#          ]
#     )
#
#     c1 = ft.Switch(label="Shiny", value=False, on_change=stwSprite)
#
#     itemsSuperior = [
#         ft.Container(botonAzul, width=80, height=80),
#         ft.Container(width=40, height=40,
#                      bgcolor=ft.colors.RED_200, border_radius=50),
#         ft.Container(width=40, height=40,
#                      bgcolor=ft.colors.YELLOW, border_radius=50),
#         ft.Container(width=40, height=40,
#                      bgcolor=ft.colors.GREEN, border_radius=50),
#         ft.Container(c1, width=40, height=60,
#                      alignment=ft.alignment.center_right),
#     ]
#
#     spritePokemon = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
#
#     image = ft.Image(
#         src=spritePokemon, scale=10, width=30, height=30, top=350 / 2, right=550/2
#     )
#
#     itemCentral = ft.Stack([
#         ft.Container(width=600, height=400,
#                      bgcolor=ft.colors.WHITE, border_radius=30),
#         ft.Container(width=550, height=350,
#                      bgcolor=ft.colors.BLACK, top=25, left=25, border_radius=30),
#         image,
#     ])
#
#     triangulo = ft.canvas.Canvas([
#         ft.canvas.Path([
#             ft.canvas.Path.MoveTo(40, 0),
#             ft.canvas.Path.LineTo(0, 50),
#             ft.canvas.Path.LineTo(80, 50)
#         ],
#             paint=ft.Paint(style=ft.PaintingStyle.FILL),
#         )
#     ],
#         height=50,
#         width=80)
#
#     flechaSuperior = ft.Container(
#         triangulo, width=80, height=50, on_click=btnGetPokemon)
#
#     flechas = ft.Column([
#         flechaSuperior,
#         # Convertir los grados que se quiere rotar en radiaes 180º = 3.14159 pi
#         ft.Container(triangulo, rotate=ft.Rotate(
#             angle=3.14159), width=80, height=50, on_click=btnGetPokemon)
#     ])
#
#
# # Continuar con el texto minuto 19:15
#
#     texto = ft.Text(
#         value="Not Found!",
#         color=ft.colors.BLACK,
#         size=22,
#     )
#
#     itemInferior = [ft.Container(width=50, ),  # Margen Izquierdo
#                     ft.Container(texto, padding=20, width=400, height=370,
#                                  bgcolor=ft.colors.GREEN, border_radius=20),
#                     ft.Container(width=30),  # Margen Derecho
#                     ft.Container(flechas, width=80, height=120),
#                     ]
#
#     superior = ft.Container(
#         content=ft.Row(itemsSuperior),
#         width=600,
#         height=80,
#         margin=ft.margin.only(top=40),
#     )
#     centro = ft.Container(content=itemCentral, width=600, height=400,
#                           margin=ft.margin.only(top=40), alignment=ft.alignment.center)
#     inferior = ft.Container(
#         content=ft.Row(itemInferior), width=600, height=400, margin=ft.margin.only(top=40)
#     )
#
#     col = ft.Column(spacing=0, controls=[superior, centro, inferior])
#
#     container = ft.Container(
#         col,
#         width=720,
#         height=1280,
#         bgcolor=ft.colors.RED,
#         alignment=ft.alignment.top_center,
#     )
#     await page.add_async(container)
#     await blink()
#
#



