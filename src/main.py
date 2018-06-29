import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as sksw
from sklearn import metrics

# Create or import dataset
def get_data():
    '''
    Import a sample dataset
    '''
    return pd.read_csv('data/bob_dylan_sample_dataset.csv')


def create_sample_dataset(test_artist, exact=False):
    '''
    Creates a sample dataset of from the 500K song
    lyric dataset for the specified band/artist
    along with a random sample of songs for comparison data.

    Parameters
    ----------
    band: name of artist or band to be used in your analysis
    exact: boolean, default False
        Whether to filter by an exact match or a string that contains the inputted artist/band value

    Returns
    -------
    .csv file containing all of the songs of the specified
    artist and a random sample (minimum 50 songs) of other
    songs from the dataset.
    '''
    dataset_location = 'data/every-song-you-have-heard-almost/Lyrics*.csv'
    full_dataset = pd.concat(
        [pd.read_csv(f) for f in glob.glob(dataset_location)])
    full_dataset.drop_duplicates(
        ['Band', 'Song', 'Lyrics'], inplace=True)
    if exact:
        artist_dataset = full_dataset[full_dataset['Band'].str.match(
            test_artist, case=False)].copy()
        rand_sample_dataset = full_dataset[~full_dataset['Band'].str.match(
            test_artist, case=False)].sample(max(len(artist_dataset), 50))
    else:
        artist_dataset = full_dataset[full_dataset['Band'].str.contains(
            test_artist, case=False)].copy()
        rand_sample_dataset = full_dataset[~full_dataset['Band'].str.contains(
            test_artist, case=False)].sample(max(len(artist_dataset), 50))
    del full_dataset
    # drop duplicates at band/artist level
    artist_dataset.drop_duplicates('Lyrics', inplace=True)
    artist_dataset['Test_Artist'] = 1
    rand_sample_dataset['Test_Artist'] = 0
    sample_dataset = pd.concat(
        [artist_dataset, rand_sample_dataset]).copy()
    write_csv_df(sample_dataset, test_artist)
    return sample_dataset


def write_csv_df(sample_dataset, test_artist):
    '''
    Checks to see if filename already exists
    '''
    filename = test_artist.replace(' ', '_').lower()+'_sample_dataset.csv'
    files_present = glob.glob(filename)
    if not files_present:
        sample_dataset.to_csv(filename, index=False)
    else:
        overwrite = input(
            f'{filename} already exists. Do you want to overwrite? (Y/N) \n')
        if overwrite[0].lower() == 'y':
            sample_dataset.to_csv(filename, index=False)
        else:
            print('Data was not saved.')

# pipeline for the model
def set_pipeline(X_train, y_train,):
    lyrics_pipeline = Pipeline([
        ('convert_lyrics', CountVectorizer(analyzer=clean_lyrics)),
        ('tf-idf', TfidfTransformer()),
        ('naive_bayes', MultinomialNB())
    ])
    return lyrics_pipeline


# split data between test and training data
def data_test_train_split(df, X_col='Lyrics', y_col='Test_Artist', size=0.3):
    X_train, X_test, y_train, y_test = train_test_split(
        df[X_col], df[y_col], test_size=size)
    return X_train, X_test, y_train, y_test


def make_predictions(pipeline, X_test):
    return pipeline.predict(X_test)


# Clean and tokenize dateset using the Bag of Words method
def vectorize_lyrics(dataset):
    '''
    Create a vectro of every word in the data set aligned with the number of times each word appears in each document
    '''
    return CountVectorizer(analyzer=clean_lyrics).fit(dataset['Lyrics'])


def clean_lyrics(lyrics, stopwords=sksw):
    '''Removes noise from song lyrics to improve comparability.

    Steps
    -----
    1. remove punctuation
    2. remove stopwords from provided dictionary
    3. return list of clean word list from lyrics

    Parameters
    ----------
    lyrics: string of lyrics to be cleaned
    stopwords: dictionary of stopwords to exclude from model, default sksw from sklearn
    '''
    rm_punct = ''.join(
        [char for char in lyrics if char not in string.punctuation])
    return [word.lower() for word in rm_punct.split() if word.lower() not in stopwords]


def bag_of_words_counts(dataset, n=20):
    '''
    Returns the nth most common words in the dataset
    '''
    sum_words = np.asarray(transform_vect(dataset).sum(axis=0)).ravel().tolist()
    counts_df = pd.DataFrame({'word': vectorize_lyrics(
        dataset).get_feature_names(), 'count': sum_words})
    return counts_df.sort_values(by='count', ascending=False).head(n)


def sample_bow_vector(dataset, n=5):
    '''
    Display a sample box of words sparse matrix from n songs. Max 10.
    '''
    bow_samp = dataset.sample(min(n, 10))
    bow_data = CountVectorizer().fit_transform(bow_samp['Lyrics']).toarray()
    bow_cols = CountVectorizer().fit(bow_samp['Lyrics']).get_feature_names()
    bow_df = pd.DataFrame(data=bow_data, columns=bow_cols)
    return bow_df


def sparse_matrix(dataset):
    sparsity = (100.0 * transform_vect(dataset).nnz /
                (transform_vect(dataset).shape[0] * transform_vect(dataset).shape[1]))
    print(f'Shape of Sparse Matrix: {transform_vect(dataset).shape}')
    print(f'Amount of Non-Zero occurences: {transform_vect(dataset).nnz}')
    print(f'Sparcity of Matrix: {sparsity:.3f}')


def transform_vect(dataset):
    return vectorize_lyrics(dataset).transform(dataset['Lyrics'])


# TF-IDF calculations
def td_idf_counts(dataset, n=20):
    '''
    Returns the nth highest weighted words in the dataset
    '''
    tfidf_weights = TfidfTransformer().fit_transform(transform_vect(dataset))
    weights = np.asarray(tfidf_weights.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'word': vectorize_lyrics(
        dataset).get_feature_names(), 'weight': weights})
    return weights_df.sort_values(by='weight', ascending=False).head(n)


# the code below definitely needs to be cleaned up
def sample_tf_idf_vector(dataset, n=5):
    '''
    Display a sample tf-idf matrix from n songs. Max 10.
    '''
    pd.options.display.float_format = '{0:.2%}'.format
    tfidf_samp = dataset.sample(min(n, 10))
    conv_1 = CountVectorizer(analyzer=clean_lyrics).fit(tfidf_samp['Lyrics'])
    conv_2 = conv_1.transform(tfidf_samp['Lyrics'])
    conv_3 = TfidfTransformer().fit(conv_2)
    tfidf_data = conv_3.transform(conv_2).toarray()
    tfidf_cols = TfidfVectorizer(analyzer=clean_lyrics).fit(
        tfidf_samp['Lyrics']).get_feature_names()
    tfidf_df = pd.DataFrame(data=tfidf_data, columns=tfidf_cols)
    return tfidf_df


# Calculate Results
def print_classification_information(y_test, y_predict):
    print(f'Accuracy: {metrics.accuracy_score(y_test, y_predict):.4f}')
    print(f'Precision: {metrics.precision_score(y_test, y_predict):.4f}')
    print(f'Recall: {metrics.recall_score(y_test, y_predict):.4f}')
    print(f'F1-Score: {metrics.f1_score(y_test, y_predict):.4f}')


def confusion_matrix(y_test, y_predict):
    return metrics.confusion_matrix(y_test, y_predict)


# perform the analysis
def main():
    sample_dataset = get_data()
    X_train, X_test, y_train, y_test = data_test_train_split(sample_dataset)
    lyrics_pipeline = set_pipeline(X_train, y_train)
    lyrics_pipeline.fit(X_train, y_train)
    y_predictions = make_predictions(lyrics_pipeline, X_test)
    print_classification_information(y_test, y_predictions)
    print(bag_of_words_counts(sample_dataset))
    sample_bow_vector(sample_dataset)
    # confusion_matrix(y_test, y_predict)




if __name__ == '__main__':
    main()
