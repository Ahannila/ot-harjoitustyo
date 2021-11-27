from tkinter.constants import S
from ui.login_view import LoginView
from ui.create_user import Create_user
from tkinter import Tk 



class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None


    def start(self):
        self.show_login_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view = None

    def show_login_view(self):
        lg = LoginView(self.root)
        lg.show_login_view()

    def show_create_account(self):
        cw = Create_user(self.root)
        cw.show_create_user()

