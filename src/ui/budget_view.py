from tkinter import ttk, constants

from entities.user import User
from services.budget_service import Budget_calculator
#from services.budget_service import Budget_calculator, InvalidCreds


class ViewOfBudgets:
    def __init__(self) -> None:
        pass

class Budget_View:
    def __init__(self, root, login_view):
        self.root = root
        self._frame = None
        self.login_view = login_view
        self.create_expense_entry = None
        #self.user = Budget_calculator.get_user(self)

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    #def initialize_hello(self):
    #    user_label = ttk.Label(master=self._frame,
    #    text= 'logged in as {self.user.username}')

    #    user_label.grid(padx=5, pady=5)

    def show_expenses(self):
        expenses_label = ttk.Label(self._frame, text="Current monthly expenses")
        expenses_label.grid(row=2, sticky=(constants.E), padx=15, pady=5)

    def create_expense(self):
        expense = self.expense_entry.get()

        try:
            Budget_calculator.add_expense(self.user,expense)
    
        except:
            print("ERROR")

    def init_header(self):
        income_button = ttk.Button(master=self._frame,
                                   text="Add income")
        expense_button = ttk.Button(master=self._frame,
                                    text="Add expense", 
                                    command=self.create_expense())

     
        expense_button.grid(row=2, sticky=(constants.W), padx=5, pady=5)
        income_button.grid(row=4, sticky=(constants.W), padx=5, pady=5)

    def initialize(self):
        self._frame = ttk.Frame(self.root)
        heading_label = ttk.Label(self._frame, text='Budget9000')

        self.expense_entry = ttk.Entry(master=self._frame)
        self.expense_entry.grid(row=3, sticky=(constants.W), padx=5, pady=5)


        #self.initialize_hello(
        self.init_header()
        self.show_expenses()
        heading_label.grid(row=1, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=400)
