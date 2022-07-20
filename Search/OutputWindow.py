import tkinter as tk
from tkinter import ttk
from tkinter import *

from OutputFunctions import *

"""
Tkinter py class for outputting search results
i'd adapt this to the search window but trying to read and write to text 
files and widgets sequentially does not seem to play nice in tkinter
however, not a lot of things do!
"""


class OutputApp(ttk.Frame):

    def __init__(self):
        ttk.Frame.__init__(self)

        # setting up widgets
        self.create_widgets()

    def create_widgets(self):

        # Making the main panel and setting up the window
        # Panedwindow
        self.paned_window = ttk.PanedWindow(self)
        self.paned_window.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Panel frame
        self.panel_frame = ttk.Frame(self.paned_window, padding=5)
        self.paned_window.add(self.panel_frame, weight=1)

        # Creating a title
        self.title = ttk.Label(text="Recipe Search", font=("-family", "Lemon Milk", "-size", 22, "-weight", "bold"))
        self.title.pack(pady=5)

        # Add tabs
        # Notebook
        self.notebook = ttk.Notebook(self.panel_frame)
        self.notebook.pack(fill="both", expand=True)

        # Tab one
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Full List")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.tab_1, orient='vertical')
        self.scrollbar.pack(side="right", fill="y")

        # Creating textbox to store results
        self.textbox = Text(self.tab_1, yscrollcommand=self.scrollbar.set, height=15, width=100)
        write_to_gui(self)

        # Setting scrollbar to change yview of textbox
        self.scrollbar.config(command=self.textbox.yview)
        self.textbox.config(state='disabled')
        self.textbox.pack()

        # Tab two
        self.tab_2 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_2.columnconfigure(index=index, weight=1)
            self.tab_2.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_2, text="Meal Plan")

        # Scrollbar
        self.scrollbar_2 = ttk.Scrollbar(self.tab_2, orient='vertical')
        self.scrollbar_2.pack(side="right", fill="y")

        # Creating textbox to store results
        self.textbox_2 = Text(self.tab_2, yscrollcommand=self.scrollbar_2.set, height=15, width=100)
        write_mealplan_to_gui(self)

        # Setting scrollbar to change yview of textbox
        self.scrollbar_2.config(command=self.textbox_2.yview)
        self.textbox_2.config(state='disabled')
        self.textbox_2.pack()


# Creating tkinter window
def output_window():
    root = tk.Tk()
    root.title("Recipe Search")
    root.resizable(False, False)

    # Set the look and feel
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = OutputApp()  # Calling the widgets class
    app.pack(fill="both", expand=True)

    # set the midsize and position window in middle
    root.update()
    root.minsize(root.winfo_width() + 10, root.winfo_height() + 10)
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()  # call tk mainloop
