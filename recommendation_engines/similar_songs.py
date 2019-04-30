import sys,os
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import elastic
# Based on the data



class Similar():
    def __init__(self):
        try:
            self.similar_songs_model = pickle.load(open('./saved_models/closest_songs_model.sav', 'rb'))
            self.artist_info = pickle.load(open('./saved_models/artist_info.sav', 'rb'))
        except FileNotFoundError:
            results_dictionary = elastic().search(index='songs',size=100)['hits']['hits']
            data = pd.DataFrame([song['_source']['doc'] for song in results_dictionary])
            self.artist_info = data[['artist','title']]
            emotions = data[['anger','fear','joy','sadness','surprise']]
            similar_songs_model = NearestNeighbors(n_neighbors=5)
            self.similar_songs_model = similar_songs_model.fit(emotions)
            pickle.dump(self.similar_songs_model, open('./saved_models/closest_songs_model.sav', 'wb'))
            pickle.dump(self.artist_info, open('./saved_models/artist_info.sav', 'wb'))
            
    def predict(self,emotion_array):
        _,indecies = self.similar_songs_model.kneighbors([emotion_array])
        return [dict(self.artist_info.iloc[row]) for row in range(len(indecies[0]))]
if __name__ == "__main__":
    test = Similar()
    print(test.predict([0.3,0.4,0.7,0.9,0.7]))