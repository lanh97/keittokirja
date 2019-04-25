from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField, TextAreaField, HiddenField

class IngredientForm(FlaskForm):
    details = TextAreaField("Details")
  
    class Meta:
        csrf = False

class IngredientsForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    details = TextAreaField("Details")
    

    class Meta:
        csrf = False