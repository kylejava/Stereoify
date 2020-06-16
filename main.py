import requests
from flask import Flask, render_template, flash, request
from keys import *
import sys
import spotipy
import spotipy.util as util
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
    return render_template('index.html')

@app.route('/results' , methods = ['GET' , 'POST'])
def results():
    token = util.prompt_for_user_token("125125",
                                      scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(limit=15, offset=0, time_range='long_term')
        tracks = []
        for item in results['items']:
            track = item['album']
            if(track['name'] + ' - ' + track['artists'][0]['name']) in tracks:
                print("Already In list")
            else:
                tracks.append(track['name'] + ' - ' + track['artists'][0]['name'])
        length = len(tracks) - (len(tracks) % 10)
    return render_template('results.html' , length = length , tracks = tracks)


if __name__ == "__main__":
    app.run(debug=True)
