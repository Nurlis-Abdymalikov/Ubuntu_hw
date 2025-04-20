import flet as ft

def main(page: ft.Page):
    page.title = "Трекер расходов"
    expenses = []
    name_input = ft.TextField(label="Описание расхода", width=300)
    amount_input = ft.TextField(label="Сумма", width=150)
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
        expense_list.controls.append(ft.Text(f"{name}: {amount} сом"))
        current_total = float(total_text.value)
        total_text.value = str(current_total + amount)
        name_input.value = ""
        amount_input.value = ""
        page.update()

    page.add(
        ft.Row([name_input, amount_input, ft.ElevatedButton(text="Сохранить", on_click=add_expense)]),
        expense_list,
        ft.Text("Общая сумма расходов:", size=16),
        total_text
    )

ft.app(target=main)
print('hello')