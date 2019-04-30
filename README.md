# GN Test Back-End API


This API was made to solve the issue of sentiment analysis for emotion detecion in lyrical corpi.

This API serves up 2 recommendation engines that do the following:

- Song Emotion Endpoint

  - Given a string as an input, this makes use of a multiclass ElasticNet regressor to determine the following emotions for a given song:
    - Anger 
    - Fear
    - Joy
    - Sadness
    - Surprise
    
- Similar Songs

 - Given a JSON of emotions that a given song could contain, this uses the K-Nearest Neighbors algorithm to retrieve songs that are nearest in distance to the emotional values submitted. This returns:
 
    - Artist Name
    - Song title



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

To get started with Using this API please refer to :
https://github.com/Novandev/gn_api/wiki

### Prerequisites

This package requires Python 3 to be installed

### Installing

1. Clone the repo

```
git clone https://github.com/Novandev/gn_api.git
```

2. Install dependencies from project root folder (Please utilize virtualenv, or pipenv)

```
pip install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](https://nodejs.org/en/) - The Python backend Framework
* [SK-Learn](https://expressjs.com/) - Machine Learning Framework
* [Pandas](https://pandas.pydata.org/) - DataFrame and Analysis Framework
* [AWS ElasticSearch](https://aws.amazon.com/elasticsearch-service/) - Document storage and retrieval 
* [IndicoIo](https://indico.io/) - Sentiment Analysis API 


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/) for details on our code of conduct, and the process for submitting pull requests to us.

 

## Authors

* ** Novan Adams ** - * Data Scientist and App Developer * - [Novandev](https://github.com/Novandev)

See also the list of [contributors](https://github.com/Novandev/CAH-BackEnd/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [https://www.gifnote.com/] - Gifnote
