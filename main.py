from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the secret secret key'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/item")
def item():
    return render_template("item.html")


@app.route("/consoles/sega-gen")
def sega():
    return render_template("sega-gen.html")


@app.route("/consoles/psp")
def psp():
    return render_template("psp.html")


@app.route("/consoles/gameboy_color")
def gbc():
    return render_template("gbc.html")


if __name__ == '__main__':
    app.run(debug=True)

