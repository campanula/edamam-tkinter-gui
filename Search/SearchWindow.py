import tkinter as tk
from tkinter import *
from tkinter import ttk

from Placeholder import PlaceholderEntry
from SearchFunctions import *

dietary = "None"  # Setting global val, ugly but it works
# don't plan on ever expanding this w/ tkinter, so it's fine

"""
Tkinter py class for setting up window searches are performed in
I now understand why nobody wants to use Tkinter anymore
"""


class SearchApp(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self)

        self.combo_list = ["Cuisine Type (Optional)", "American", "Asian", "British", "Caribbean", "Central Europe",
                           "Chinese", "Eastern Europe", "French",
                           "Indian", "Italian", "Japanese", "Kosher", "Mediterranean", "Mexican", "Middle Eastern",
                           "Nordic", "South American", "South East Asian"]  # Setting up list for choosing cuisine

        # Setting up widgets
        self.create_widgets()

    def create_widgets(self):
        # Making the main panel and setting up the window
        # Panedwindow
        self.paned_window = ttk.PanedWindow(self)
        self.paned_window.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Panel frame
        self.panel_frame = ttk.Frame(self.paned_window, padding=5)
        for index in [0, 1]:
            self.panel_frame.columnconfigure(index=index, weight=1)
            self.panel_frame.rowconfigure(index=index, weight=1)
        self.paned_window.add(self.panel_frame, weight=1)

        # Creating a title
        self.title = ttk.Label(text="Recipe Search", font=("-family", "Lemon Milk", "-size", 22, "-weight", "bold"))
        self.title.pack(pady=5)

        # Radiobox frame for buttons
        self.radiobox_frame = ttk.LabelFrame(self.panel_frame, text="Dietary Requirements (Optional)", padding=(20, 10))
        self.radiobox_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(0, 10), sticky="nsew"
        )

        # Function for recording which radiobutton is selected and setting it as the dietary value
        def selected():
            num = var.get()
            global dietary
            dietary = radiobox_switch(num)
            print("Diet value " + dietary)
            return dietary

        var = IntVar()  # Setting radiobuttons to be a IntVar

        # Radiobuttons

        # This is horrible but apparently tkinter ignores the look&feel for radiobuttons/checkbuttons if I try and
        # load them from a list and code more dynamically, so it has to be done for now :(
        # If I find a solution to it ignoring my theme I'll fix this
        self.check_1 = ttk.Radiobutton(
            self.radiobox_frame, text="Vegetarian", variable=var, value=1, command=selected
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.check_2 = ttk.Radiobutton(
            self.radiobox_frame, text="Vegan", variable=var, value=2, command=selected
        )
        self.check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.check_3 = ttk.Radiobutton(
            self.radiobox_frame, text="Alcohol-free", variable=var, value=3, command=selected
        )
        self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.check_4 = ttk.Radiobutton(
            self.radiobox_frame, text="Gluten-free", variable=var, value=4, command=selected)
        self.check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        self.check_5 = ttk.Radiobutton(
            self.radiobox_frame, text="Dairy-free", variable=var, value=5, command=selected)
        self.check_5.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        # Create frame for input widgets
        self.widgets_frame = ttk.Frame(self.panel_frame)
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(0, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Don't move this func, has to be nested here to work right with Tkinter /shrug
        # Func to get input from entry form as a string when button is pressed
        def get_input():
            string = self.entry.get()
            print("Ingredient " + string)
            get_ingredient(string, self, dietary)

        # Setting up label
        self.label = ttk.Label(self.panel_frame, text="Edamam recipe search API", justify="right", font=("-size", 10))
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        # Creating entry widget for entering ingredient
        self.entry = PlaceholderEntry(self.widgets_frame, placeholder="Please enter an ingredient")
        self.entry.grid(row=0, column=0, padx=50, pady=(0, 10), sticky="ew")

        # Creating combobox and setting it to readonly
        self.combobox = ttk.Combobox(
            self.widgets_frame, state="readonly", values=self.combo_list
        )
        self.combobox.current(0)  # Set default value to 0 in array
        self.combobox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Creating submit button
        self.button = ttk.Button(self.widgets_frame, text="Submit", style="Accent.TButton", command=get_input)
        self.button.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")


# Creating tkinter window
def search_window():
    root = tk.Tk()
    root.title("Recipe Search")
    root.resizable(False, False)

    # Set the look and feel
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = SearchApp()  # Calling the widgets class
    app.pack(fill="both", expand=True)

    # set the midsize and position window in middle
    root.update()
    root.minsize(root.winfo_width() + 10, root.winfo_height() + 10)
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()  # call tk mainloop
