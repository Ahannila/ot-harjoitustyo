from tkinter import Frame, ttk, constants, StringVar
from budget_service import Budget_calculator, InvalidCreds
class Create_user:
    def __init__(self, root, login_view):
        self._root = root
        self.login_view = login_view
        #self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self.show_create_user()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def create_user_handler(self):
        user = self._username_entry.get()

        try:
            Budget_calculator.create_account(self, user)
            username_label = ttk.Label(master=self._frame , text="Account created")
            username_label.grid(padx=5, pady=5)
            

        except InvalidCreds:
            print("ERROR")

    def init_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_create_user(self):
        self._frame = ttk.Frame(master=self._frame)

        heading_label = ttk.Label(master=self._frame, text='Create user')
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        self.init_username_field()

        create_account_button = ttk.Button(master=self._frame,
            text='Create account',
            command=self.create_user_handler)

        create_back_button = ttk.Button(master=self._frame,
            text='Back to login',
            command=self.login_view)


        create_account_button.grid(columnspan=3, padx=5,pady=5)
        create_back_button.grid(columnspan=4, padx=5, pady=5)