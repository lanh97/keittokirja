from application import db
from application.models import Base

from sqlalchemy.sql import text


class Recipe(Base):

    name = db.Column(db.String(144), nullable=False)
    details = db.Column(db.String(144))
    cookinginstructions = db.Column(db.String(1000))

    recipeingredient = db.relationship("RecipeIngredient", backref='recipe', lazy=True, cascade="all, delete-orphan")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name ,details ,cookinginstructions):
        self.name = name
        self.details = details
        self.cookinginstructions = cookinginstructions

    @staticmethod
    def find_recipes_with_no_ingredients():
        stmt = text("SELECT recipe.id, recipe.name FROM recipe"
                     " LEFT JOIN recipe_ingredient ON recipe_ingredient.recipe_id = recipe.id"
                     " GROUP BY recipe.id"
                     " HAVING COUNT(recipe_ingredient.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def recipes_ingredients(para):
        stmt = text("SELECT ingredient.name FROM ingredient, recipe, recipe_ingredient"
        " WHERE recipe_id = recipe_ingredient.recipe_id" 
        " AND ingredient.id = recipe_ingredient.ingredient_id" 
        " AND recipe.id = :para"
        " GROUP BY ingredient.name;").params(para = para)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response
