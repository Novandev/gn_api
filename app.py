import sys,os
from flask import Flask,Response,request
import json

from recommendation_engines.similar_songs import Similar
from recommendation_engines.song_emotions import Emotions
app = Flask(__name__)

similar_engine = Similar()
emotion_engine = Emotions()
emotions = ['anger','fear','joy','sadness','surprise']

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/similar-songs', methods=['POST'])
def get_similar_songs():
    content = request.get_json()
    predict_values = [content[emotions[i]] for i in range(len(emotions))]
    predict_list = list(map(float, predict_values))
    predictions = similar_engine.predict(predict_list)
    return Response(json.dumps(predictions))

@app.route('/song-emotions', methods=['POST'])
def get_song_emotions():
    content = request.get_json()
    predictions = emotion_engine.predict([content['lyrics']])[0]
    prediction_dict = dict(zip(emotions,predictions))
    return Response(json.dumps(prediction_dict))

app.run(host='127.0.0.1', port= 5000)