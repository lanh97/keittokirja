from application import db
from application.models import Base


class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)
    details = db.Column(db.String(144))
    per = db.Column(db.Integer)

    recipeingredient = db.relationship("RecipeIngredient", backref='ingredient', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, details):
        self.name = name
        self.details = details
