from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.stadium import Stadium
import repositories.stadium_repository as stadium_repository

stadiums_blueprint = Blueprint("stadiums", __name__)

@stadiums_blueprint.route("/stadiums")
def stadiums():
    pass 