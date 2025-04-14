# hw_3
# import flet as ft

# def main(page: ft.Page):
#     page.title = 'Список друзей'
#     input_text = ft.TextField(label='Введите текст')
#     items = []

#     def add_clicked(e):
#         items.append(input_text.value)
#         print('Список друзей')
#         print(items)
#         input_text.value = ''
#         page.update()
#     page.add(input_text, ft.ElevatedButton(text='Добавить', on_click = add_clicked),)

# ft.app(target=main)

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