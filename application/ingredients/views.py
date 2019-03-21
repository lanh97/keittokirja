from application import app, db
from flask import redirect, render_template, request, url_for
from application.ingredients.models import Ingredient

@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
def ingredients_form():
    return render_template("ingredients/new.html")

@app.route("/ingredients/", methods=["POST"])
def ingredients_create():
    ingre = Ingredient(request.form.get("name"))

    db.session().add(ingre)
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))