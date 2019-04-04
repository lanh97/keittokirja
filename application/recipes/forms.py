from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField

class RecipeForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    details = StringField("Details")
    cookinginstructions = StringField("Cooking Instructions")
  
    class Meta:
        csrf = False