from application import app, db
from flask import redirect, render_template, request, url_for, session
from flask_login import current_user, login_required, LoginManager
from application.recipes.forms import RecipeForm, RecipeupdateForm
from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.recipesingredient.models import RecipeIngredient


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    recip = Recipe(form.name.data, form.details.data,
                   form.cookinginstructions.data)
    
    recip.account_id = current_user.id
    db.session().add(recip)
    db.session().commit()

    return redirect(url_for("recipes_form"))


@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipe_ingredient(recipe_id):
    session["recipeid"] = recipe_id
    return render_template("recipeingredient/list.html", ingredients=Ingredient.query.all(), form=RecipeupdateForm(), find_ingre=Recipe.recipes_ingredients(recipe_id))


@app.route("/recipes/details", methods=["POST"])
@login_required
def recipe_update():
    form = RecipeupdateForm(request.form)
    id = session["recipeid"]
    recip = Recipe.query.get(id)

    none = ""

    if form.details == none:
        pass
    else:
        recip.details = form.details.data

    if form.cookinginstructions == none:
        pass
    else:
        recip.cookinginstructions = form.cookinginstructions.data
    
    db.session().commit()
    return redirect(url_for("recipes_index"))


@app.route("/recipe/details", methods=["POST"])
def recipe_details():
    recip_id = session["recipeid"]
    ingred = request.form.get("ingredient")
    recipingre = RecipeIngredient()
    recipingre.ingredient_id = ingred
    recipingre.recipe_id = recip_id
    db.session().add(recipingre)
    db.session().commit()
    return redirect(url_for("recipe_ingredient", recipe_id=recip_id))


@app.route("/recipe/<recipe_id>/delete", methods=["POST"])
@login_required
def recipe_delete(recipe_id):

    recip = Recipe.query.get(recipe_id)

    if recip.account_id != current_user.id:
        return redirect(url_for("index"))

    db.session().delete(recip)
    db.session().commit()

    return redirect(url_for("recipes_index"))

