import flet as ft

def main(page: ft.Page):
    page.title = "Трекер расходов"
    expenses = []

    name_input = ft.TextField(label="Название расхода", width=300)
    amount_input = ft.TextField(label="Сумма расхода", width=150)
    total_text = ft.Text(value="0", size=20, weight="bold", color=ft.colors.BLUE)
    expense_list = ft.Column()

    def add_expense(e):
        name = name_input.value
        amount_str = amount_input.value
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError()
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Сумма должна быть положительным числом!"))
            page.snack_bar.open = True
            page.update()
            return
        
        expense_item = ft.Row([
            ft.Text(name, size=16, weight="bold", color=ft.colors.BLACK),
            ft.Text(f"{amount}", size=16, color=ft.colors.BLUE),
            ft.Icon(name=ft.icons.EDIT, color=ft.colors.BLUE),
            ft.Icon(name=ft.icons.DELETE, color=ft.colors.RED)
        ], spacing=10)

        expense_list.controls.append(expense_item)

        current_total = float(total_text.value)
        total_text.value = str(current_total + amount)

        name_input.value = ""
        amount_input.value = ""
        page.update()

    page.add(
        ft.Text("Ваши расходы", size=30, weight="bold"),
        ft.Row([name_input, amount_input, ft.ElevatedButton(text="Добавить", on_click=add_expense)]),
        ft.Text("Общая сумма расходов:", size=16),
        total_text,
        expense_list
    )

ft.app(target=main)