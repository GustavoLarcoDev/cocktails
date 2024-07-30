from django.shortcuts import render, redirect, get_object_or_404
from recipes.models import Recipe
from recipes.forms import RecipeForm



def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    context = {
        "form": form,
    }
    return render(request, "recipes/create.html", context)


def edit_coktail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect(show_recipe, id=id)
    else:
        form = RecipeForm(instance=recipe)
    context = {
        "recipe_list": recipe,
        "post_form": form,
    }
    return render(request, "recipes/edit.html", context)


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)
