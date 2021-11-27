from login_view import LoginView
from tkinter import Tk 



class UI:
    def __init__(self, root):
        self.root = root

    
    def start(self):
        self.show_login_view()

    def show_login_view(self):
        lg = LoginView(self.root)
        lg.show_login_view()


