# Binary Classification Using Bob Dylan Lyrics

## Background

After discovering the [Every song you have heard (almost)!](https://www.kaggle.com/artimous/every-song-you-have-heard-almost) song lyric dataset on Kaggle.com which includes over 500,000 song lyrics, I had a grandiose idea of determining which is a better predictor of song popularity: song lyrics or music composition. After being persuaded **(and rightfully so)** this project was a little ambitious for a first capstone, I was still curious if I could discover any meaning full data using song lyrics.

Even though our course has not covered Natural Language Processing, I was allowed to use this dataset for my capstone project as long as I understood that I would have to teach myself several NLP techniques over a short period of time. After spending a decent amount of time researching the subject, I decided to take the risk and proceed with this dataset.

### ~~Hot Dog/Not Hot Dog~~ Bob Dylan/ Not Bob Dylan

After deciding to use song lyrics for my capstone, I had to pivot and decide on a topic that used concepts we have learned about in class along with teaching myself some NLP techniques. After some contemplating, I remembered Bob Dylan is famous for not only writing his own music, but also writing many very famous songs that were made famous by other artists. Below is sample list of those songs. I knew he had written many songs but after some research, the total number of songs he is credited with writing is somewhere between 350 and 650 songs!!!. The Kaggle dataset has him listed as the artist for over 600 unique songs which gives me a  Below is sample list of those songs:

#### Songs Written by Bob Dylan made famous by other artists:
* All Along the Watchtower - Jimi Hendrix (or DMB for some)
* Mr. Tambourine Man - The Byrds
* It Ain't Me Babe - The Turtles
* Wagon Wheel - Old Crow Medicine Show (or Darius Rucker)
* Love is Just a Four Letter Word - Joan Baez
* The Mighty Quinn (Quinn the Eskimo) - Manfred Mann
* Farewell or Fare Thee Well - most recently featured in the Coen Brother's Film "Inside Llewen Davis"

Eventually I decided the topic **"Bob Dylan/Not Bob Dylan"** with the goal of building a classifcation model to predict if a song was written in fact written by Bob Dylan.

### Process
1. Clean the data
* Demonstration Data
![demo_data](images/demo_data.png)

2. Tokenize all words using bag of words method:
* Demo Data:
![demo_bow](images/demo_bow.png)

* Actual Data:
![bow_count](images/bow_count.png)

3. Add weights to each word using the TF-IDF method:
* Demo Data:
![demo_bow](images/demo_tfidf.png)

* Actual Data:
![tfidf_weight](images/tfidf_weight.png)

4. Test the data using the Naive Bayes method:

**Given the song is Bob Dylan, what is the probability that we see that specific word?**


## Results

| Stat | Score |
| ----------- | ----------- |
| Accuracy | 69.2% |
| Precision | 61.0% |
| Recall | 92.3% |
| F1-Score | 73.6% |

### Confusion Matrix
| 92 | 107 |
| ----------- | ----------- |
| 14 | 168 |

<!-- ## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p> -->
