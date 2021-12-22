"""
from ui.budget_view import Budget_View
from tkinter import constants, ttk
from matplotlib import pyplot as plt
class Graph_View:
    def __init__(self, root, budget_view):
        self.root = root
        self.budget_view = budget_view
        self.frame = None

        self.initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize_graph(self):
        labels = 'A', 'B', 'C', 'D'
        sizes = [15, 30, 45, 10]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        back_label = ttk.Label(master=self.frame,text='Back')
        back_label.grid()
        plt.show()

    def initialize(self):
        self.frame = ttk.Frame(self.root)

 
        self.initialize_graph() 
"""