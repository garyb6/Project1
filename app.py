from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.stadiums_controller import stadiums_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(stadiums_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)