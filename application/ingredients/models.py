from application import db
from application.models import Base


class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)
    lisatiedot = db.Column(db.String(144))
    yksikkohinta = db.Column(db.Integer)

    def __init__(self, name, lisatiedot):
        self.name = name
        self.lisatiedot = lisatiedot
