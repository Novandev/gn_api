import sys,os, nltk,string,re
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Lasso,MultiTaskLasso,ElasticNet
from sklearn.feature_extraction.text import CountVectorizer # To get a vector of occurences
from sklearn.preprocessing import StandardScaler # To scale data for regression algorithm
from nltk.corpus import stopwords
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from config import elastic
import pickle
nltk.download('stopwords')
# cleaning the stopwords from the corpus will help in predictions later
stop_words = set(stopwords.words('english'))

vectorize = CountVectorizer()
scaler = StandardScaler(with_mean=False)
multiple_class_regression = MultiOutputRegressor(ElasticNet(alpha=0.0001,max_iter=10000,random_state=1999, selection='random',normalize=True))


def clean_stop_words(string):
    return ' '.join([word for word in string.split(' ') if word not in stop_words])
class Emotions():
    def __init__(self):
        try:
            self.emotions_model = pickle.load(open('./saved_models/emotions_model.sav', 'rb'))
        except FileNotFoundError:
            results_dictionary = elastic().search(index='songs',size=100)['hits']['hits']
            data = pd.DataFrame([song['_source']['doc'] for song in results_dictionary])
            y = data[['anger','fear','joy','sadness','surprise']]
            y = [list(y.iloc[row]) for row in range(len(y))]
            X = list(data['cleaned_lyrics'])
            X = [clean_stop_words(lyrics) for lyrics in X]
            X = vectorize.fit_transform(X)
            self.emotions_model = multiple_class_regression.fit(X, y)
            pickle.dump(self.emotions_model, open('./saved_models/emotions_model.sav', 'wb'))
            
    def predict(self,song_string):
        song_to_predict = vectorize.transform(song_string)
        return self.emotions_model.predict(song_to_predict)
if __name__ == "__main__":
    test = Emotions()
    test.predict(['yeah yeah oh love thing  working day long im ready come home mm mm guys roll eyes dont realize want want say im wrapped around finger dont understand got diamond hand  baby love thing whoa baby love thing yeah  sure could hang around complain way things ought yeah theres trouble world youre girl whose open arms really need thats come runnin side let em call crazy cant denied  baby love thing whoa ah baby love thing yeah  last name thing explained make feel inside way hold every night  love thing whoa oh baby love thing yeah  go love thing  say im wrapped around finger dont understand got diamond hand baby love thing whoa oh baby love thing yeah come love thing whoa oh baby love thing yeah oh love thing whoa oh sugar love thing aint diamond ring love thing whoa oh baby love thing love love love thing'])