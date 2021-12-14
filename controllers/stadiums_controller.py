from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.stadium import Stadium
import repositories.stadium_repository as stadium_repository
import repositories.country_repository as country_repository 

stadiums_blueprint = Blueprint("stadiums", __name__)

@stadiums_blueprint.route("/stadiums")
def stadiums():
    stadiums = stadium_repository.select_all()
    return render_template("stadiums/index.html", all_stadiums = stadiums)

#NEW
@stadiums_blueprint.route("/stadiums/new", methods=['GET'])
def new_stadium():
    countries = country_repository.select_all()
    return render_template("stadiums/new.html", all_countries = countries)

# CREATE
@stadiums_blueprint.route("/stadiums",  methods=['POST'])
def create_stadium():
    name    = request.form['name']
    category = request.form['category']
    country  = country_repository.select(request.form['country_id'])
    visited = request.form['visited']
    stadium = Stadium(name, category, country, visited)
    stadium_repository.save(stadium)
    return redirect('/stadiums')

# SHOW??
@stadiums_blueprint.route("/stadiums/<id>", methods=['GET'])
def show_stadium(id):
    stadium = stadium_repository.select(id)
    return render_template('stadiums/show.html', stadium = stadium)

# EDIT
# GET '/stadiums/<id>/edit'
@stadiums_blueprint.route("/stadiums/<id>/edit", methods=['GET'])
def edit_stadium(id):
    stadium = stadium_repository.select(id)
    countries = country_repository.select_all()
    return render_template('stadiums/edit.html', stadium = stadium, all_countries = countries)

# UPDATE
# PUT '/stadiums/<id>'
@stadiums_blueprint.route("/stadiums/<id>", methods=['POST'])
def update_stadium(id):
    name = request.form['name']
    category = request.form['category']
    country  = country_repository.select(request.form['country_id'])
    visited = request.form['visited']
    stadium = Stadium(name, category, country, visited, id)
    print(stadium.country.name)
    stadium_repository.update(stadium)
    return redirect('/stadiums')

# DELETE
# DELETE '/stadiums/<id>'
@stadiums_blueprint.route("/stadiums/<id>/delete", methods=['POST'])
def delete_stadium(id):
    stadium_repository.delete(id)
    return redirect('/stadiums') 

@stadiums_blueprint.route("/stadiums/")
def stadiums_visited():
    stadiums = stadium_repository.select_visited()
    return render_template("stadiums/visited.html", all_stadiums = stadiums)

@stadiums_blueprint.route("/stadiums/to_visit/")
def stadiums_to_visit():
    stadiums = stadium_repository.select_to_visit()
    return render_template("stadiums/to_visit.html", all_stadiums = stadiums)
