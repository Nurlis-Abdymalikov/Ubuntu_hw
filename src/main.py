import flet as ft

def main(page: ft.Page):
    page.title = "Hi Word"

    def change_name(e):
        print(name_input.value)

    def click_button(e):
        print(name_input.value)
    
    name_input = ft.TextField(
        label='enter your name',
        on_change=change_name
    )

    button = ft.ElevatedButton('save', on_click=click_button)


    page.add(name_input, button)


ft.app(main)