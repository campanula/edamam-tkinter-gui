import os

"""
py class for storing functions used with OutputWindow.py
"""


# Print all recipes to GUI
def write_to_gui(self):
    self.textbox.delete("1.0", "end")  # clear textbox

    path = 'output/out.txt'
    if os.stat(path).st_size == 0:  # True if empty
        self.textbox.insert('end', "No results")  # if file is empty print no results
    else:
        with open(path, 'r') as f:  # Open text file
            for line in f:
                self.textbox.insert('end', line)  # Print text file content to GUI textbox
        # Close text file
        f.close()


# Print meal-plans to GUI
def write_mealplan_to_gui(self):
    self.textbox_2.delete("1.0", "end")  # clear textbox

    path = 'output/meal-plan.txt'
    if os.stat(path).st_size == 0:  # True if empty
        self.textbox_2.insert('end', "No results")  # if file is empty print no results
    else:
        self.textbox_2.insert('end', 'Lets plan the meals for this week!\n\n')
        with open(path, 'r') as f:  # Open text file
            for line in f:
                self.textbox_2.insert('end', line)  # Print text file content to GUI textbox

        # Close text file
        f.close()
