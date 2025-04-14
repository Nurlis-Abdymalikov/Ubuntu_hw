import flet as ft

def main(page: ft.Page):
    # title = ft.Text("To-do list", size=30, weight=ft.FontWeight.BOLD)
    page.title = "Hello World"

    def change_name(e):
        print(name_input.value)

    def click_button(e):
        print(name_input.value)

    
    name_input = ft.TextField(
        label='enter your name',
        on_change=change_name
    )

    def listt(e):
        list = name_input.value

    list = ft.Text(list)

    button = ft.ElevatedButton('save', on_click=click_button)
    

    page.add(name_input, button,list)

ft.app(main) 