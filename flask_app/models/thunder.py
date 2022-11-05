from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
# cmd D multiple cursers

class Track:
    db = "sound_of_thunder_schema"
    def __init__(self,data):
        self.id = data['id']

        self.track_number = data['track_number']
        self.song_title = data['song_title']
        self.song_duration = data['song_duration']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def show_track_list(cls):
        # Select Query to pull info from database #
        query = "SELECT * FROM track_list"
        # Variable to connect to the database I want to pull data from #
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances #
        tracks =[]
        for dict in results:
            # Variable to store the class instances #
            tracks.append( cls(dict) )
        return tracks

    @classmethod
    def play_track(cls,data):
        query = "SELECT * FROM track_list WHERE track_number = %(track_number)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_song_title(cls,data):
        query = "SELECT * FROM track_list WHERE song_title = %(song_title)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
