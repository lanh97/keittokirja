from application import app, db
from flask import redirect, render_template, request, url_for, session
from flask_login import login_required
from application.recipes.forms import RecipeForm
from application.recipes.models import Recipe


@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/reicipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    recip = Recipe(form.name.data, form.lisatiedot.data,
                   form.cookinginstruction.data)
    db.session().add(recip)
    db.session().commit()

    return redirect(url_for("recipes_form"))
