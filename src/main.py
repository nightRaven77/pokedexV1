import flet as ft
import requests



def main(page: ft.Page):
    page.title = "Pokédex Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.window.width = 450

    # Variables para almacenar datos del Pokémon
    pokemon_name = ft.Text("Bulbasaur", size=28, weight=ft.FontWeight.BOLD)
    pokemon_id = ft.Text("#001", size=20)
    pokemon_types = ft.Row (alignment=ft.MainAxisAlignment.CENTER)
    pokemon_image = ft.Image(
        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        width=200,
        height=200,
    )
    pokemon_stats = ft.Column()

    # Función para buscar Pokémon
    def search_pokemon(e):
        query = search_field.value.lower().strip()
        print(query)
        if query:
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query}")
                if response.status_code == 200:
                    data = response.json()
                    # Actualizar los datos
                    pokemon_name.value = data["name"].capitalize()
                    pokemon_id.value = f"#{data["id"]}"
                    if

                    pokemon_image.src = data["sprites"]["other"]["official-artwork"][f"{sprite}"]

                    # se actualizan los tipos
                    pokemon_types.controls.clear()
                    for type_data in data["types"]:
                        print(type_data["type"]["name"].capitalize())
                        pokemon_types.controls.append(
                            ft.Container(
                                content=ft.Text(
                                    type_data["type"]["name"].capitalize(),
                                    color="white",
                                    weight=ft.FontWeight.BOLD,
                                ),
                                padding=10,
                                border_radius=10,
                                bgcolor=get_type_color(type_data["type"]["name"]),
                                margin=5,
                            ),
                        )
                    # se actualizan estadisticas
                    pokemon_stats.controls.clear()
                    for stat in data["stats"]:
                        pokemon_stats.controls.append(
                            ft.Row(
                                controls=[
                                    ft.Text(stat["stat"]["name"].replace("-", " ").capitalize(), width=100),
                                    ft.Text(stat["base_stat"], weight=ft.FontWeight.BOLD),
                                    ft.ProgressBar(value=stat["base_stat"] / 200, width=200),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            )
                        )
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("¡Pokémon no encontrado!"), open=True)
                    page.update()
            except Exception as ex:
                print(ex)
                page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}"), open=True)
                page.update()

    # Función para obtener el color según el tipo de Pokémon
    def get_type_color(pokemon_type):
        colors = {
            "normal": "#A8A878",
            "fire": "#F08030",
            "water": "#6890F0",
            "electric": "#F8D030",
            "grass": "#78C850",
            "ice": "#98D8D8",
            "fighting": "#C03028",
            "poison": "#A040A0",
            "ground": "#E0C068",
            "flying": "#A890F0",
            "psychic": "#F85888",
            "bug": "#A8B820",
            "rock": "#B8A038",
            "ghost": "#705898",
            "dragon": "#7038F8",
            "dark": "#705848",
            "steel": "#B8B8D0",
            "fairy": "#EE99AC",
        }
        return colors.get(pokemon_type, "#777777")  # Color por defecto

    # Barra de búsqueda
    search_field = ft.TextField(
        label="Nombre o ID del Pokémon",
        hint_text="Ej: Pikachu o 25",
        width=300,
        border_radius=20,
        autofocus=True,
        on_submit=search_pokemon,
    )
    search_button = ft.ElevatedButton(
        text="Buscar",
        icon=ft.Icons.SEARCH,
        on_click=search_pokemon,
    )
    switch_sprite = ft.Switch(
        label="Shiny",
        value=False
    )

    # Diseño principal
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[search_field, search_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[switch_sprite],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[pokemon_id, pokemon_name],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Divider(),
                                pokemon_image,
                                ft.Divider(),
                                pokemon_types,
                                ft.Divider(),
                                ft.Text("Estadísticas", size=20, weight=ft.FontWeight.BOLD),
                                pokemon_stats,
                            ],
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=20,
                    ),
                    elevation=10,
                    width=400,
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


# Ejecutar la app
ft.app(target=main)
