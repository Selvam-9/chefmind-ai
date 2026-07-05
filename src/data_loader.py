import json
from pathlib import Path

def load_recipes():
    """
    Load recipes from the json
    """
    data_path = Path('data/final_recipes.json')

    with open(data_path,'r',encoding='utf-8') as file:
        recipes = json.load(file)
    return recipes
