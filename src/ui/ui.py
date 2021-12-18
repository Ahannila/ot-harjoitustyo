from ui.login_view import LoginView
from ui.create_user import Create_user
from ui.budget_view import Budget_View
from ui.graph_view import Graph_View

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_login_view()
        # self.show_create_account()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()
        self.current_view = LoginView(
            self.root, self.show_create_account, self.show_budget_service)
        self.current_view.pack()

    def show_create_account(self):
        self.hide_current_view()
        self.current_view = Create_user(self.root, self.show_login_view)
        self.current_view.pack()

    def show_budget_service(self):
        self.hide_current_view()
        self.current_view = Budget_View(self.root, self.show_login_view, self.show_graph_view)
        self.current_view.pack()

    def show_graph_view(self):
        self.hide_current_view()
        self.current_view = Graph_View(self.root, self.show_budget_service)
        self.current_view.pack()