from tkinter import ttk, constants
from entities.user import User
from services.budget_service import budget_calculator, InvalidCreds



class Budget_View:
    def __init__(self, root, login_view):
        self.root = root
        self._frame = None
        self.login_view = login_view
        self.create_expense_entry = None
        self.user = budget_calculator.get_user()

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def remove_by_id(self, expense):
        id = budget_calculator.get_expense_id(expense)
        budget_calculator.remove_expense(id)
        pass

    def init_sum_of_budgets(self):
        sum = str(budget_calculator.get_sum_of_expenses())
        expenses_label = ttk.Label(self._frame, text="Current monthly expenses:  "+sum+"€")
        expenses_label.grid(row=1,sticky=(constants.W), padx=5, pady=5)

    def init_budget_item(self, budget):
        self.init_sum_of_budgets()

        expense_id = budget_calculator.get_expense_id(budget)

        set_budget_button = ttk.Button(
            master=self._frame,
            text=budget,
            command= lambda: self.remove_expense(set_budget_button, expense_id)
        )

        set_budget_button.grid(
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )


    def remove_expense(self, button, expense_id):
        button.destroy()
        budget_calculator.remove_expense(expense_id)
        self.init_sum_of_budgets()


    def show_expenses(self):
        expenses = budget_calculator.get_expenses()
    
        self.remove_by_id(22)
        for expense in expenses:
            print(budget_calculator.get_expense_id(expense))
            print(expense)
            self.init_budget_item(expense)  

    def create_expense_handler(self):
        expense = self.expense_entry.get()

        try:
            budget_calculator.add_expense(expense)
            self.init_budget_item(expense)

        except:
            print("Error while creating expense")


    def initialize(self):
        self._frame = ttk.Frame(master=self.root)
        heading_label = ttk.Label(self._frame, text='Budget9000')

        self.show_expenses()

        self.expense_entry = ttk.Entry(master=self._frame)
        self.expense_entry.grid(row=2, sticky=(constants.E), padx=5, pady=5)

        expense_button = ttk.Button(master=self._frame,
                            text="Add expense", 
                            command=self.create_expense_handler)

        expense_button.grid(row=2,sticky=(constants.W), padx=5, pady=5)
        heading_label.grid(row=0, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)
        self._frame.grid_columnconfigure(1, weight=1)
