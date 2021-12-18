from tkinter import ttk, constants
from services.budget_service import budget_calculator


class Budget_View:
    def __init__(self, root, login_view, graph_view):
        self.root = root
        self._frame = None
        self.login_view = login_view
        self.graph_view = graph_view
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
        

    def init_sum_of_budgets(self):
        sum = str(budget_calculator.get_sum_of_expenses())
        expenses_label = ttk.Label(self._frame, text="Current monthly expenses:  "+sum+"€")
        expenses_label.grid(row=1,sticky=(constants.W), padx=5, pady=5)

    def init_budget_item(self, name, budget):
        self.init_sum_of_budgets()

        expense_id = budget_calculator.get_expense_id(budget)

        set_budget_button = ttk.Button(
            master=self._frame,
            text= name + str(budget),
            command= lambda: self.remove_expense(set_budget_button, expense_id)
        )

        set_budget_button.grid(
            row=expense_id+3,
            column=0,
            padx=5,
            pady=5,
            sticky=(constants.W)
        )

    def remove_expense(self, button, expense_id):
        button.destroy()
        budget_calculator.remove_expense(expense_id)
        self.init_sum_of_budgets()


    def show_expenses(self):
        expenses = budget_calculator.get_expenses()
        for expense in expenses:
            id = budget_calculator.get_expense_id(expense)
            name = budget_calculator.get_expense_name_with_id(id)
            self.init_budget_item(name ,expense)

    def create_expense_handler(self):
        expense = self.expense_entry.get()
        expense = "-"+expense
        try:
            budget_calculator.add_budget(self.name_entry.get(), expense)
            self.init_budget_item(self.name_entry.get(),expense)
            self.clear_text()
        except:
            print("Error while creating expense")

    def create_income_handler(self):
        income = self.income_entry.get()
        try:
            budget_calculator.add_budget(self.name_entry.get(),income)
            self.init_budget_item(self.name_entry.get(),income)
            self.clear_text()
        except:
            print("Error while creating expense")

    def clear_text(self):
        self.expense_entry.delete(0, 'end')
        self.income_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')

    def move_to_graph(self):
        try:
            self.graph_view()
        except:
            print("error")

    def initialize(self):
        self._frame = ttk.Frame(master=self.root)
        heading_label = ttk.Label(self._frame, text='Budget9000')

        self.show_expenses()

        self.expense_entry = ttk.Entry(master=self._frame)
        self.name_entry=ttk.Entry(master=self._frame)

        expense_button = ttk.Button(master=self._frame,
                            text="Add expense",
                            command=self.create_expense_handler)

        
        name_entry_label = ttk.Label(master=self._frame, text="Enter the name of the budget")

        self.income_entry = ttk.Entry(master=self._frame)
        income_button = ttk.Button(master=self._frame,
                            text="Add income",
                            command=self.create_income_handler)

        graph_button = ttk.Button(master=self._frame,
                            text='View graph of budgets',
                            command=self.graph_view)
        graph_button.grid()

        
        expense_button.grid(row=2,sticky=(constants.W), padx=5, pady=5)
        self.expense_entry.grid(row=2, sticky=(constants.E), padx=5, pady=5)

        income_button.grid(row=2,column=1, padx=5, pady=5)
        self.income_entry.grid(row=2, column=2,padx=5, pady=5)

        name_entry_label.grid(row=1, column=2,padx=5, pady=5)
        self.name_entry.grid(row=1,column=3, sticky=(constants.E))

        heading_label.grid(row=0, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)
        self._frame.grid_columnconfigure(1, weight=1)


        
