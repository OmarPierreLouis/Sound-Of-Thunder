from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.thunder import Track


@app.route("/")
def dashboard(): 

    return render_template("dashboard.html")

@app.route("/tracklist")
def tracklist():
    # Calling the class method #
    tracks = Track.show_track_list()
    # Create a varable in your return statment to parse through in your template #
    return render_template("tracklist.html", tracks = tracks)


@app.route("/playtrack/<track_number>/<song_title>")
def play_track(track_number, song_title):
    data = {
        'song_title': song_title
    }
    track_list = Track.get_song_title(data)
    return render_template("playtrack.html", track_list = track_list) 
