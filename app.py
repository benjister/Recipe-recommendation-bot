from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Spoonacular API key
API_KEY = 'fcbfac8f8c8b4d8489a6d8a422d34fb0'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['POST'])
def recommendation():
    query = request.form['category']
    recipes = get_recipes(query)
    if recipes:
        return render_template('recommendation.html', category=query, recipes=recipes)
    else:
        return render_template('error.html', message="No recipes found for this query.")

@app.route('/recipe', methods=['POST'])
def recipe():
    recipe_id = request.form['recipe_id']
    recipe_info = get_recipe_info(recipe_id)
    if recipe_info:
        # Remove HTML tags from instructions
        recipe_info['instructions'] = remove_html_tags(recipe_info['instructions'])
        return render_template('recipe.html', recipe_info=recipe_info)
    else:
        return render_template('error.html', message="Recipe information not available.")

def get_recipes(query):
    url = f"https://api.spoonacular.com/recipes/search?query={query}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return None

def get_recipe_info(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

if __name__ == "__main__":
    app.run(debug=True)
