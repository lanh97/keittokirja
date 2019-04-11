from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField

class IngredientForm(FlaskForm):
    details = StringField("Details")
  
    class Meta:
        csrf = False

class IngredientsForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    details = StringField("Details", [validators.Length(min=2)])

    class Meta:
        csrf = False