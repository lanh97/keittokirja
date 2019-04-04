from application import db
from application.models import Base


class Recipe(Base):

    name = db.Column(db.String(144), nullable=False)
    details = db.Column(db.String(144))
    cookinginstruction = db.Column(db.String(1000))

    def __init__(self, name, cookinginstruction):
        self.name = name
        self.cookinginstruction = cookinginstruction
