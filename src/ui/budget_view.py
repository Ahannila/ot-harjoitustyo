import sqlite3
from tkinter import Label, Listbox, ttk, constants

from entities.user import User
from services.budget_service import budget_calculator, InvalidCreds


class ViewOfBudgets:
    def __init__(self, root, budgets):
        self.root = root
        self.budgets = budgets
        self.frame = None
        
        self.initialize()
        
    def init_budget_item(self,budget):
        item_frame = ttk.Frame(master=self.frame)
        Label = ttk.Label(master=item_frame, text=budget.content)
    
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        #for budget in self.budgets:
        

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

    #def initialize_hello(self):
    #    user_label = ttk.Label(master=self._frame,
    #    text= 'logged in as '+self.user.username)

    #    user_label.grid(padx=5, pady=5, sticky=(constants.S, constants.N))

    def init_budget_item(self, budget):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=self._frame, text=budget)

        set_done_button = ttk.Button(
            master=self._frame,
            text='remove',
        )

        label.grid(column=1, padx=5, pady=5, sticky=constants.E)

        set_done_button.grid(
            column=1,
            padx=5,
            pady=5,
            sticky=constants.E
        )
        item_frame.grid_columnconfigure(0, weight=1)

    def show_expenses(self):
        expenses_label = ttk.Label(self._frame, text="Current monthly expenses")
        expenses_label.grid(row=2, sticky=(constants.E), padx=5, pady=5)

        budget = budget_calculator.print_expense()
        for budgets in budget:
            print(budgets)
            self.init_budget_item(budgets)
   
        #expense_label = ttk.Label(master=self._frame, text=budget)
        #expense_label.grid(row=3, sticky=(constants.E), padx=15, pady=5)
        #try:
        #    budget_calculator.print_expense()
        #except sqlite3.Error as error:
        #    print("Error show expenses"+ error)


    def create_expense_handler(self):
        expense = self.expense_entry.get()

        try:
            budget_calculator.add_expense(expense)
            self.init_budget_item(expense)

        except:
            print("ERROR2")


    def init_income_field(self):
        income_button = ttk.Button(master=self._frame,
                                   text="Add income")

        income_button.grid(row=4, sticky=(constants.W), padx=5, pady=5)

    def initialize(self):
        self._frame = ttk.Frame(master=self.root)
        heading_label = ttk.Label(self._frame, text='Budget9000')


        self.show_expenses()
        #self.initialize_hello()

        self.expense_entry = ttk.Entry(master=self._frame)
        self.expense_entry.grid(row=3, sticky=(constants.W), padx=5, pady=5)

        expense_button = ttk.Button(master=self._frame,
                            text="Add expense", 
                            command=self.create_expense_handler)

        expense_button.grid(row=2, sticky=(constants.W), padx=5, pady=5)
        heading_label.grid(row=1, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=400)
