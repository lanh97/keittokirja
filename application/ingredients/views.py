from application import app, db
from flask import redirect, render_template, request, url_for, session
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm, IngredientsForm
from flask_login import login_required


@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients=Ingredient.query.all())


@app.route("/ingredients/new/")
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientsForm())


@app.route("/ingredients/<ingredient_id>/", methods=["GET"])
def singredient_index(ingredient_id):
    session["ingredientid"] = ingredient_id
    return render_template("ingredients/id.html", form=IngredientForm())


@app.route("/ingredients/lisatiedot", methods=["POST"])
@login_required
def ingredient_lisatiedot():
    form = IngredientForm(request.form)
    id = session["ingredientid"]
    ingre = Ingredient.query.get(id)
    ingre.lisatiedot = form.lisatiedot.data
    db.session().commit()
    return redirect(url_for("ingredients_index"))


@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientsForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form = form)

    ingre = Ingredient(form.name.data, form.lisatiedot.data)
    db.session().add(ingre)
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))
