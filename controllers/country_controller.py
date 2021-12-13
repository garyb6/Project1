from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

#NEW
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("country/new.html", all_countries = countries)

# # CREATE
# @stadiums_blueprint.route("/stadiums",  methods=['POST'])
# def create_stadium():
#     name    = request.form['name']
#     category = request.form['category']
#     country  = country_repository.select(request.form['country_id'])
#     visited = request.form['visited']
#     stadium = Stadium(name, category, country, visited)
#     stadium_repository.save(stadium)
#     return redirect('/stadiums')

# SHOW??
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_countries(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)