from tkinter import ttk, constants
#from services.budget_service import Budget_calculator, InvalidCreds


class Budget_View:
    def __init__(self, root, login_view):
        self.root = root
        self._frame = None
        self.login_view = login_view
        self._username_entry = None


        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(self.root)
        heading_label = ttk.Label(self._frame, text='Budget9000')

        income_button = ttk.Button(master=self._frame,
                                   text="Add income")

        expense_button = ttk.Button(master=self._frame,
                                    text="Add expense")

        heading_label.grid(row=1, padx=5, pady=5)
        expense_button.grid(row=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        income_button.grid(row=3, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=400)