from tkinter import ttk, StringVar, constants
from budget_service import Budget_calculator, InvalidCreds


class LoginView:
    def __init__(self, root, create_user_view):
        self.root = root
        #self.root.resizable(False, False)
        self.frame = None
        self.create_user_view = create_user_view
        self.username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

    def pack(self):
        pass


    def login_handler(self):
        username = self.username_entry.get()
        
        try:
            Budget_calculator.login(self,username)
            username_label = ttk.Label(master=self.root, text="Logged in")
            username_label.grid(padx=5, pady=5)

        except InvalidCreds:
            self.show_error('Invalid username')


    #def show_error(self, message):
    #    self._error_variable.set()
    #    self._error_label.grid()

    def init_username_field(self):
        username_label = ttk.Label(master=self.root, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
    #def init_password_field(self):
    #    password_label = ttk.Label(master=self.root, text="Password")
    #    password_entry = ttk.Entry(master=self.root)

    #    password_label.grid(padx=5, pady=5)
    #    password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_login_view(self):
        heading_label = ttk.Label(master=self.root, text="Login")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        self.init_username_field()

    #    self.init_password_field()

        login_button = ttk.Button(master=self.root, 
        text="Login", 
        command=self.login_handler)
        
        button_create_account = ttk.Button(master=self.root,
         text="Create account",
         command=self.create_user_view)

        #heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_create_account.grid(columnspan=3, padx=5, pady=5)

