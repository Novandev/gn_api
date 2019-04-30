import sys,os
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import elastic
# Based on the data



class Similar():

    """
    This class is used to find silimar songs by emotional score using K-Nearest Neighbors.
    It first checks for the presence of a pretrained model in .sav format to cu down on processing time.
    if one is not found, it pulls data from ElasticSearch to train and fit the model.
    
    """
    def __init__(self):
        try: # load both models
            self.similar_songs_model = pickle.load(open('./saved_models/closest_songs_model.sav', 'rb'))
            self.artist_info = pickle.load(open('./saved_models/artist_info.sav', 'rb'))
        except FileNotFoundError: # if  either model isnt present then...
            results_dictionary = elastic().search(index='songs',size=100)['hits']['hits']
            data = pd.DataFrame([song['_source']['doc'] for song in results_dictionary])
            self.artist_info = data[['artist','title']]
            emotions = data[['anger','fear','joy','sadness','surprise']]
            similar_songs_model = NearestNeighbors(n_neighbors=5)
            self.similar_songs_model = similar_songs_model.fit(emotions)
            # The following writes the pickle files out
            pickle.dump(self.similar_songs_model, open('./saved_models/closest_songs_model.sav', 'wb'))
            pickle.dump(self.artist_info, open('./saved_models/artist_info.sav', 'wb')) # this needs to be here so artist info can be gather for processing later
            
    def predict(self,emotion_array):
        """
        Used for the API endpoint, this returns the artists and songs that are simmilar based on our KNN model
        
        """
        _,indecies = self.similar_songs_model.kneighbors([emotion_array])
        return [dict(self.artist_info.iloc[row]) for row in range(len(indecies[0]))] #r returns a dictionart of the artists and songs that match 
if __name__ == "__main__":
    test = Similar()
    print(test.predict([0.3,0.4,0.7,0.9,0.7]))