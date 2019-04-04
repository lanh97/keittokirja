from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField

class IngredientForm(FlaskForm):
    lisatiedot = StringField("Lisätiedot")
  
    class Meta:
        csrf = False

class IngredientsForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    lisatiedot = StringField("Lisätiedot", [validators.Length(min=2)])

    class Meta:
        csrf = False