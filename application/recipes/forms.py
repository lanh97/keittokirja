from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField, TextAreaField

class RecipeForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    details = TextAreaField("Details")
    cookinginstructions = TextAreaField("Cooking Instructions")

    class Meta:
        csrf = False

class RecipeupdateForm(FlaskForm):
    details = TextAreaField("Details")
    cookinginstructions = TextAreaField("Cooking Instructions")

    class Meta:
        csrf = False