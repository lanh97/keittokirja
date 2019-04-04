from application import db
from application.models import Base


class RecipeIngredient(Base):

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                           nullable=False)
                           
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
                           nullable=False)