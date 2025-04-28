import flet as ft
from database import ExpenseDB

def main(page: ft.Page):
    page.title = "Трекер расходов"
    db = ExpenseDB()

    name_input = ft.TextField(label="Название расхода", width=300)
    amount_input = ft.TextField(label="Сумма расхода", width=150)
    total_text = ft.Text(value=str(db.get_total_amount()), size=20, weight="bold", color=ft.colors.BLUE)
    expense_list = ft.Column(expand=True, scroll='always')

    def refresh_expenses():
        expense_list.controls.clear()
        for expense_id, name, amount in db.get_all_expenses():
            expense_item = ft.Row([
                ft.Text(name, size=16, weight="bold", color=ft.colors.BLACK),
                ft.Text(f"{amount}", size=16, color=ft.colors.BLUE),
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color=ft.colors.BLUE,
                    icon_size=20,
                    # пока что без функции редактирования
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED,
                    icon_size=20,
                    data=expense_id,          # сохраним ID расхода
                    on_click=delete_expense    # обработчик нажатия
                ),
            ], spacing=10)
            expense_list.controls.append(expense_item)

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

        db.add_expense(name, amount)
        refresh_expenses()
        total_text.value = str(db.get_total_amount())

        name_input.value = ""
        amount_input.value = ""
        page.update()

    def delete_expense(e):
        expense_id = e.control.data
        db.delete_expense(expense_id)
        refresh_expenses()
        total_text.value = str(db.get_total_amount())
        page.update()

    refresh_expenses()

    page.add(
        ft.Text("Ваши расходы", size=30, weight="bold"),
        ft.Row([name_input, amount_input, ft.ElevatedButton(text="Добавить", on_click=add_expense)]),
        ft.Text("Общая сумма расходов:", size=16),
        total_text,
        expense_list
    )

ft.app(target=main)
