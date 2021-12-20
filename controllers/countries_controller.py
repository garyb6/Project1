from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("countries/new.html")

@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name    = request.form['name']
    continent = request.form['continent']
    language = request.form['language']
    description = request.form['description']
    visited = request.form['visited']
    rating = request.form['rating']
    country = Country(name, continent, language, description, visited, rating)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_countries(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name    = request.form['name']
    continent = request.form['continent']
    language = request.form['language']
    description = request.form['description']
    visited = request.form['visited']
    rating = request.form['rating']
    country = Country(name, continent, language, description, visited, rating, id)
    country_repository.update(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')

@countries_blueprint.route("/countries/")
def countries_visited():
    countries = country_repository.select_visited()
    return render_template("countries/visited.html", all_countries = countries)

@countries_blueprint.route("/countries/to_visit/")
def countries_to_visit():
    countries = country_repository.select_to_visit()
    return render_template("countries/to_visit.html", all_countries = countries)