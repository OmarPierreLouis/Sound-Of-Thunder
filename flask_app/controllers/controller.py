from flask_app import app
from flask import render_template, redirect, session, request


@app.route("/")
def dashboard():

    return render_template("dashboard.html")

@app.route("/tracklist")
def tracklist():

    return render_template("tracklist.html")

@app.route("/playone")
def playone():

    return render_template("playone.html")
