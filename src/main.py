import flet as ft
def main(page: ft.Page):
    page.title = "Список друзей"
    name_field = ft.TextField(label='Имя') 
    age_field = ft.TextField(label='Возраст', keyboard_type=ft.KeyboardType.NUMBER)
    friends = []
    def add_friend(e):
        name = name_field.value.strip()
        try:
            age = int(age_field.value)
        except ValueError:
            age = 0
        friend = {"name": name, "age": age}
        friends.append(friend)
        print("Список друзей")
        print(friends)
        name_field.value = ""
        age_field.value = ""
        page.update()
 
    page.add(
        name_field,
        age_field,
        ft.ElevatedButton(text="Добавить друга", on_click=add_friend),
    )
ft.app(target=main)