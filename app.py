import sys,os
from flask import Flask,Response,request
import json

from recommendation_engines.similar_songs import Similar
from recommendation_engines.song_emotions import Emotions
app = Flask(__name__)

similar_engine = Similar() # Similarity Engine
emotion_engine = Emotions() # Emotions Engine
emotions = ['anger','fear','joy','sadness','surprise'] # List used to grab values from JSON

@app.route('/')
def hello_world():
    return 'Hello, Gifnote'

# Route for getting similar songs
@app.route('/similar-songs', methods=['POST'])
def get_similar_songs():
    content = request.get_json()
    predict_values = [content[emotions[i]] for i in range(len(emotions))] # Grab only the emotions in the request that are also in the list
    predict_list = list(map(float, predict_values)) # This comes in JSON string so converting them to floats 
    predictions = similar_engine.predict(predict_list) # Predict
    return Response(json.dumps(predictions))
# Route for getting a songs emotions
@app.route('/song-emotions', methods=['POST'])
def get_song_emotions():
    content = request.get_json()
    predictions = emotion_engine.predict([content['lyrics']])[0] # predictions for this algorithm are in a list so grab prediction from position 0
    prediction_dict = dict(zip(emotions,predictions)) # Predict
    return Response(json.dumps(prediction_dict))

app.run(host='127.0.0.1', port= 5000)