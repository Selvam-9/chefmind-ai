import os
import  sys
from os.path import abspath
# Add the project root to sys.path
current_dir = abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

def create_document(recipe):
    """
    Create a single recipe document
    """
    ingredients_string = "".join(f'{ingredient.strip().lower()}\n' for ingredient in recipe.get('ingredients',[]))
    document = f"""title: {recipe.get('title',"")}\ningredients: {ingredients_string}\ninstructions:{" ".join(recipe.get('instructions',""))}"""
    return document

def create_documents(recipes):
    """
    Preprocess all recipes and return a list of documents
    """
    return [create_document(recipe) for recipe in recipes]  

