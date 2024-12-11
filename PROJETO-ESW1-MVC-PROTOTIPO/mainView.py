import flet as ft
from controllers.controladorRoute import ControladorRoutes

def main(page: ft.Page):
    page.title = "Sistema de Atendimento SEBRAE"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False

    controlador_routes = ControladorRoutes(page)
    page.on_route_change = controlador_routes.route_change
    page.go("/")

ft.app(target=main)
