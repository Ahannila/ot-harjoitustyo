from tkinter import ttk, StringVar, constants, Tk

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.frame = None
        self.username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None


    def login_handler(self):
        pass

    def init_username_field(self):
        username_label = ttk.Label(master=self.root, text="Username")
        self.username_entry = ttk.Entry(master=self.root)

        username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
    def init_password_field(self):
        password_label = ttk.Label(master=self.root, text="Password")
        password_entry = ttk.Entry(master=self.root)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_login_view(self):
        heading_label = ttk.Label(master=self.root, text="Login")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        self.init_username_field()

        self.init_password_field()

        button = ttk.Button(master=self.root, text="Login")
        button_create_account = ttk.Button(master=self.root, text="Create account")

        #heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_create_account.grid(columnspan=3, padx=5, pady=5)

