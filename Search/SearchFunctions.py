from tkinter.messagebox import showinfo

import requests
import config
import random

"""
py class for storing functions used with SearchWindow.py
"""


# Get Edamam API results
def request_api(ingredient, dietary, cuisineType):
    print('running')

    app_id = config.APPLICATION_ID  # getting api info from config.py file
    key = config.APPLICATION_KEY

    response = filter_api(ingredient, dietary, cuisineType, app_id, key)

    if response.status_code != 200:  # If api cannot find result, return error
        return response.text
    else:
        print("url found")  # Else continue
        data = response.json()
        return data['hits']


# Choose a url to request based on the user input entered
def filter_api(ingredient, dietary, cuisineType, app_id, key):
    # Edamam doesn't seem to lend itself to a neater way of making different api calls
    none = "Cuisine Type (Optional)"
    if dietary != "None" and cuisineType != none:  # Use dietary and cuisineType values
        url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&cuisineType={}'.format(
            ingredient, app_id, key, dietary, cuisineType)  # including the dietary value will break it now as it goes
        # over the api limit for free users :( but it's not a problem with the code, so I'll leave it

    elif dietary != "None" and cuisineType == none:  # Use dietary values
        url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(
            ingredient, app_id, key, dietary)

    elif dietary == "None" and cuisineType != none:  # Use cuisine type values
        url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&cuisineType={}'.format(
            ingredient, app_id, key, cuisineType)

    else:  # Only use ingredient value
        url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(
            ingredient, app_id, key)

    return requests.get(url)  # return api response


# Get ingredient after validation
# If string is not letters or is null, display error message.
# If letters, return true
def is_letters(string):
    if string == "Please enter an ingredient" or string is None:
        warning_null()
        return False

    elif string.isalpha():
        return True

    else:
        warning_alpha()
        return False


# check if ingredient is alpha
# if true, commence search
def get_ingredient(string, self, dietary):
    if is_letters(string):
        ingredient = string

        cuisineType = self.combobox.get()  # get cuisine type from combobox
        print("Cuisine Type " + cuisineType)
        search(ingredient, dietary, cuisineType)  # start search
        self.label.configure(text="Close window to continue")  # change label to give user instruction


# Get recipe results then print
def search(ingredient, dietary, cuisineType):
    try:
        # Get recipe results from API according to search term
        results = request_api(ingredient, dietary, cuisineType)

        # print results data to text files
        print_full(results)
        print_meal_plan(results)

    except TypeError as ex:  # general exception catcher to stop the api limit problem from causing an error
        print(ex)
        return ex


# Print meal plan results to file
def print_meal_plan(results):
    with open('output/meal-plan.txt', 'w') as f:
        f.truncate(0)  # Empty file

        if not results:  # Return if empty
            return "No results"

        # get a random meal and print it once for each day
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # print('Lets plan the meals for this week!', file=f)
        for x in weekdays:
            random_meal = random.choice(results)
            recipe = random_meal['recipe']
            print(x + "\nRecipe:", recipe['label'] + "\n       \n" + "URL: " + recipe['url'] + "\n\n   -----   \n",
                  file=f)

    # Close text file
    f.close()


# Print all results to file
def print_full(results):
    with open('output/out.txt', 'w') as f:
        f.truncate(0)  # Empty file

        if not results:  # Return if empty
            return "No results"

        # If not empty, print every result to file
        for result in results:
            recipe = result['recipe']
            print(recipe['label'])
            print(recipe['url'])

            print("Recipe: " + recipe['label'] + "\n       \n" + "URL: " + recipe['url'] + "\n\n   -----   \n",
                  file=f)  # Add results to text file

    # Close text file
    f.close()


# Switch to get radiobox output
def radiobox_switch(num):
    match num:
        case 1:
            return "Vegetarian"
        case 2:
            return "Vegan"
        case 3:
            return "Alcohol-free"
        case 4:
            return "Gluten-free"
        case 5:
            return "Dairy-free"
        case _:
            return "Error " + num


# Input validation warnings
def warning_alpha():
    showinfo("Error", "Please enter only letters")


def warning_null():
    showinfo("Error", "Please enter an ingredient")
