from tkinter import StringVar, ttk, constants
from entities.user import User
from services.budget_service import Budget_calculator, InvalidCreds


class LoginView:
    def __init__(self, root, create_user_view, auth_login):
        self.root = root
        self.root.resizable(False, False)
        self.frame = None
        self.create_user_view = create_user_view
        self.auth_login = auth_login
        self.username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self.show_login_view()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def login_handler(self):
        username = self.username_entry.get()
        password = self._password_entry.get()

        try:
            Budget_calculator.login(self,username,password)
            username_label = ttk.Label(master=self.frame, text="Logged in")
            username_label.grid(padx=5, pady=5)
            self.auth_login()
        except InvalidCreds:
            self.show_error('Wrong credentials')

    def show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def hide_error(self):
        self._error_label.grid_remove()

    def init_username_field(self):
        username_label = ttk.Label(master=self.frame, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def init_password_field(self):
        password_label = ttk.Label(master=self.frame, text="Password")
        self._password_entry = ttk.Entry(master=self.frame, show="*")

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_login_view(self):
        self.frame = ttk.Frame(master=self.root)

        heading_label = ttk.Label(master=self.frame, text="Login")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        self.init_username_field()

        self.init_password_field()
        self._error_variable = StringVar(self.frame)
        self._error_label = ttk.Label(master=self.frame, 
        textvariable=self._error_variable,
        foreground='red')

        self._error_label.grid(padx=2, pady=5)

        login_button = ttk.Button(master=self.frame,
                                  text="Login",
                                  command=self.login_handler)

        button_create_account = ttk.Button(master=self.frame,
                                           text="Create account",
                                           command=self.create_user_view)

        #self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        #heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        button_create_account.grid(columnspan=3, padx=5, pady=5)
        self.hide_error()
