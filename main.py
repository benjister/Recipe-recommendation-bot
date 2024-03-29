# -*- coding: utf-8 -*-
import random

# ANSI color codes for terminal styles
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Dictionary of recipes with their instructions
recipes = {
    "pasta": {
        "Spaghetti Carbonara": "1. Cook spaghetti according to package instructions. \n2. In a skillet, cook bacon until crispy. \n3. Whisk together eggs, Parmesan cheese, and black pepper. \n4. Drain cooked spaghetti and toss with bacon. \n5. Pour egg mixture over spaghetti and toss until coated. Serve immediately.",
        "Pesto Pasta": "1. Cook pasta according to package instructions. \n2. In a blender, combine basil, garlic, pine nuts, Parmesan cheese, and olive oil. \n3. Blend until smooth to make pesto sauce. \n4. Drain cooked pasta and toss with pesto sauce. Serve with additional Parmesan cheese if desired.",
        "Fettuccine Alfredo": "1. Cook fettuccine according to package instructions. \n2. In a saucepan, melt butter and whisk in heavy cream. \n3. Stir in grated Parmesan cheese until melted and sauce is creamy. \n4. Drain cooked fettuccine and toss with Alfredo sauce. Serve immediately."
    },
    "soup": {
        "Chicken Noodle Soup": "1. In a large pot, heat olive oil and sauté onions, carrots, and celery until softened. \n2. Add chicken broth and bring to a boil. \n3. Add cooked chicken, noodles, and seasonings. \n4. Simmer until noodles are tender. Serve hot.",
        "Tomato Basil Soup": "1. In a pot, sauté onions and garlic until fragrant. \n2. Add canned tomatoes, vegetable broth, and fresh basil. \n3. Simmer for 20-30 minutes. \n4. Use an immersion blender to puree the soup until smooth. Serve with a dollop of cream if desired.",
        "Vegetable Soup": "1. In a pot, heat olive oil and sauté onions, carrots, and celery until softened. \n2. Add vegetable broth, diced tomatoes, and mixed vegetables. \n3. Season with salt, pepper, and herbs. \n4. Simmer until vegetables are tender. Serve hot."
    },
    "salad": {
        "Caesar Salad": "1. In a bowl, whisk together lemon juice, olive oil, garlic, anchovy paste, Worcestershire sauce, and Dijon mustard. \n2. Toss romaine lettuce with the dressing until coated. \n3. Top with croutons and shaved Parmesan cheese. Serve immediately.",
        "Greek Salad": "1. In a bowl, combine chopped cucumbers, tomatoes, red onions, bell peppers, olives, and feta cheese. \n2. Drizzle with olive oil and red wine vinegar. \n3. Season with salt, pepper, and oregano. Toss to combine. Serve chilled.",
        "Caprese Salad": "1. Arrange slices of fresh tomatoes and mozzarella cheese on a serving platter. \n2. Drizzle with balsamic glaze and olive oil. \n3. Sprinkle with fresh basil leaves, salt, and pepper. Serve immediately."
    },
    "dessert": {
        "Chocolate Cake": "1. Preheat oven to 350°F (175°C). \n2. Mix flour, sugar, cocoa, baking powder, baking soda, and salt. \n3. Add eggs, milk, oil, and vanilla. Mix until smooth. \n4. Pour into a greased and floured cake pan. \n5. Bake for 30-35 minutes. Let cool before frosting.",
        "Apple Pie": "1. Preheat oven to 425°F (220°C). \n2. Mix sliced apples with sugar, flour, cinnamon, and nutmeg. \n3. Place apple mixture into a pastry-lined pie plate. \n4. Cover with top crust, seal edges, and cut slits in the top. \n5. Bake for 40-45 minutes until crust is golden brown.",
        "Cheesecake": "1. Preheat oven to 325°F (165°C). \n2. Mix graham cracker crumbs, butter, and sugar. Press into the bottom of a springform pan. \n3. Beat cream cheese until smooth. Add sugar, eggs, and vanilla. Mix well. \n4. Pour over crust. \n5. Bake for 55 minutes. Let cool before refrigerating."
    },
    "breakfast": {
        "Pancakes": "1. In a bowl, mix flour, sugar, baking powder, and salt. \n2. Whisk in milk, eggs, and melted butter. \n3. Pour batter onto a hot griddle. Cook until bubbles form. Flip and cook until golden brown.",
        "Omelette": "1. Whisk eggs, salt, and pepper. \n2. Pour into a hot skillet with melted butter. \n3. Cook until eggs are set. Add fillings like cheese, ham, and vegetables. \n4. Fold omelette in half. Serve hot.",
        "French Toast": "1. Whisk together eggs, milk, cinnamon, and vanilla. \n2. Dip bread slices into the egg mixture. \n3. Cook on a hot griddle until golden brown on both sides. Serve with syrup or powdered sugar."
    }
}

def get_recipe(category):
    """
    Function to get a random recipe from the specified category.
    """
    if category.lower() in recipes:
        recipe, instructions = random.choice(list(recipes[category.lower()].items()))
        return recipe, instructions
    else:
        return None, None

def main():
    print(bcolors.HEADER + "Welcome to Recipe Recommendation Bot!" + bcolors.ENDC)
    print("I can suggest recipes for the following categories:")
    print(bcolors.OKGREEN + "1. Pasta" + bcolors.ENDC)
    print(bcolors.OKGREEN + "2. Soup" + bcolors.ENDC)
    print(bcolors.OKGREEN + "3. Salad" + bcolors.ENDC)
    print(bcolors.OKGREEN + "4. Dessert" + bcolors.ENDC)
    print(bcolors.OKGREEN + "5. Breakfast" + bcolors.ENDC)
    print(bcolors.WARNING + "Type 'quit' to exit." + bcolors.ENDC)
    while True:
        user_input = input(bcolors.OKCYAN + "Please select a category by entering the corresponding number: " + bcolors.ENDC)
        if user_input.lower() == "quit":
            print(bcolors.FAIL + "Goodbye!" + bcolors.ENDC)
            break
        elif user_input.isdigit():
            choice = int(user_input)
            if choice >= 1 and choice <= 5:
                category = {
                    1: "pasta",
                    2: "soup",
                    3: "salad",
                    4: "dessert",
                    5: "breakfast"
                }[choice]
                recipe, instructions = get_recipe(category)
                if recipe:
                    print(bcolors.OKBLUE + f"Here's a {category} recipe you might like: {recipe}" + bcolors.ENDC)
                    print(bcolors.BOLD + "Instructions:" + bcolors.ENDC)
                    print(instructions)
                else:
                    print(bcolors.FAIL + "Sorry, I don't have any recipes for that category yet." + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "Invalid choice. Please select a number between 1 and 5." + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Invalid input. Please enter a number." + bcolors.ENDC)

if __name__ == "__main__":
    main()
