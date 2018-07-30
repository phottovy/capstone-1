import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import itertools
from tabulate import tabulate

from add_stop_words import add_stop_words, nltk_s_words
from main import get_data, set_pipeline, make_predictions, data_test_train_split, combine_stopwords

plt.style.use('seaborn-darkgrid')
plt.rcParams["patch.force_edgecolor"] = True

porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()
sksw = ENGLISH_STOP_WORDS
nltksw = nltk_s_words()
addsw = add_stop_words()
allsw = combine_stopwords


# clean dataset
def clean_full_dataset(dataset, stopwords=sksw, lemm=None, stem=None):
    clean_dataset = dataset.copy()
    clean_dataset['Lyrics'] = clean_strip_lyrics(
        clean_dataset['Lyrics'], stopwords, lemm, stem)
    clean_lyrics = clean_dataset['Lyrics']
    return clean_dataset, clean_lyrics


def clean_strip_lyrics(dataset, stopwords=sksw, lemm=None, stem=None):
    '''
    Strip punctuation and cleans the word list

    Steps
    -----
    1. remove punctuation
    2. remove stopwords from provided dictionary, default sksw list
        allsw for a combination of three sets of stopwords
    3. stem word list, default None
    4. lemmatize word list, default None
    5. return list of clean word list from lyrics

    Parameters
    ----------
    lyrics: string of lyrics to be cleaned
    stopwords: dictionary of stopwords to exclude from model, default sksw from sklearn
    '''
    rm_punct = [''.join(
        [char for char in word if char not in string.punctuation]) for word in dataset]
    rm_stop = [[word.lower() for word in words.split()if word.lower()
                not in stopwords] for words in rm_punct]
    if lemm == wordnet:
        rm_lemm = [[wordnet.lemmatize(word)
                    for word in words] for words in rm_stop]
    else:
        rm_lemm = rm_stop
    if stem == porter:
        rm_stem = [[porter.stem(word) for word in words] for words in rm_lemm]
    elif stem == snowball:
        rm_stem = [[snowball.stem(word) for word in words]
                   for words in rm_lemm]
    else:
        rm_stem = rm_lemm
    clean_lyrics = [' '.join([word for word in words]) for words in rm_stem]
    return pd.Series(clean_lyrics)


full_dataset = get_data()


# CV
def confusion_matrix_plot_cv(tn, fp, fn, tp, save_fig=False, cmap=plt.cm.Blues):
    '''
    This function prints and plots the confusion matrix.
    '''
    cm = np.array([[tp, fn], [fp, tn]])
    classes = ['True', 'False']
    plt.figure(figsize=(4, 4))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.grid(b=None)
    plt.title('Confusion Matrix', fontsize=20)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.ylabel('True label', fontsize=12)
    plt.xlabel('Predicted label', fontsize=12)
    if save_fig:
        plt.savefig('confusion_matrix.png')
    plt.show()


def my_cross_val_score(dataset, num_folds=3, stopwords=sksw, lemm=None, stem=None, max_feats=None):
    ''' Returns error for k-fold cross validation. '''
    clean_dataset, clean_lyrics = clean_full_dataset(
        dataset, stopwords, lemm, stem)
    X = clean_dataset['Lyrics']
    y = clean_dataset['Test_Artist']

    kf = KFold(n_splits=num_folds, shuffle=True)
    acc_cv = np.empty(num_folds)
    pre_cv = np.empty(num_folds)
    rec_cv = np.empty(num_folds)
    f1_cv = np.empty(num_folds)
    tn, fp, fn, tp = 0, 0, 0, 0
    index = 0
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        lyrics_pipeline = set_pipeline(X_train, y_train, max_feats)
        y_predict = make_predictions(lyrics_pipeline, X_test)
        y_probs = lyrics_pipeline.predict_proba(X_test)[:, 1]
        acc_cv[index] = metrics.accuracy_score(y_test, y_predict)
        pre_cv[index] = metrics.precision_score(y_test, y_predict)
        rec_cv[index] = metrics.recall_score(y_test, y_predict)
        f1_cv[index] = metrics.f1_score(y_test, y_predict)
        tn += metrics.confusion_matrix(y_test, y_predict).ravel()[0]
        fp += metrics.confusion_matrix(y_test, y_predict).ravel()[1]
        fn += metrics.confusion_matrix(y_test, y_predict).ravel()[2]
        tp += metrics.confusion_matrix(y_test, y_predict).ravel()[3]
        index += 1
    cols = ['Statistic', 'Result']
    acc = ['Accuracy', '{:.4f}'.format(np.mean(acc_cv))]
    pre = ['Precision', '{:.4f}'.format(np.mean(pre_cv))]
    rec = ['Recall', '{:.4f}'.format(np.mean(rec_cv))]
    f1 = ['F1-Score', '{:.4f}'.format(np.mean(f1_cv))]
    print('Classification Statistics:\n')
    print(tabulate([cols, acc, pre, rec, f1],
                   headers='firstrow', tablefmt='pipe'))
    print(np.array([[tp, fn], [fp, tn]]))
    confusion_matrix_plot_cv(tn, fp, fn, tp)


def cv_scores(max_splits=10):
    cv_range = range(2, max_splits+1)

    for num in cv_range:
        print(f'# of splits: {num}\n')
        my_cross_val_score(full_dataset, num)


# gridsearch
def gridsearch_with_output(estimator, parameter_grid, X, y):
    '''
        Parameters: estimator: the type of model (e.g. RandomForestRegressor())
                    paramter_grid: dictionary defining the gridsearch parameters
                    X_train: 2d numpy array
                    y_train: 1d numpy array

        Returns:  best parameters and model fit with those parameters
    '''
    model_gridsearch = GridSearchCV(estimator,
                                    parameter_grid,
                                    n_jobs=-1,
                                    verbose=True,
                                    refit=True,
                                    cv=4,
                                    scoring='f1')  # ['f1', 'precision', 'recall', 'accuracy'])
    model_gridsearch.fit(X, y)
    best_params = model_gridsearch.best_params_
    model_best = model_gridsearch.best_estimator_
    print("\nResult of gridsearch:")
    print("{0:<20s} | {1:<8s} | {2}".format(
        "Parameter", "Optimal", "Gridsearch values"))
    print("-" * 55)
    for param, vals in parameter_grid.items():
        print("{0:<20s} | {1:<8s} | {2}".format(str(param),
                                                str(best_params[param]),
                                                str(vals)))
    return best_params, model_best


def display_default_and_gsearch_model_results(model_default, model_gridsearch,
                                              X_test, y_test):
    '''
        Parameters: model_default: fit model using initial parameters
                    model_gridsearch: fit model using parameters from gridsearch
                    X_test: 2d numpy array
                    y_test: 1d numpy array
        Return: None, but prints out mse and r2 for the default and model with
                gridsearched parameters
    '''
    name = model_default.__class__.__name__.replace(
        'Regressor', '')  # for printing
    y_test_pred = model_gridsearch.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_test_pred)
    pre = metrics.precision_score(y_test, y_test_pred)
    rec = metrics.recall_score(y_test, y_test_pred)
    f1 = metrics.f1_score(y_test, y_test_pred)
#     print("Results for {0}".format(name))
    print("Gridsearched model acc: {:0.3f} | pre: {:0.3f} | rec = {:0.3f} | f1 = {:0.3f}".format(
        acc, pre, rec, f1))
    y_test_pred = model_default.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_test_pred)
    pre = metrics.precision_score(y_test, y_test_pred)
    rec = metrics.recall_score(y_test, y_test_pred)
    f1 = metrics.f1_score(y_test, y_test_pred)
    print("     Default model acc: {:0.3f} | pre: {:0.3f} | rec = {:0.3f} | f1 = {:0.3f}".format(
        acc, pre, rec, f1))


feats_grid = {'convert_lyrics__max_features': [
    None, 50, 100, 500, 1000, 5000, 10000, 12000]}


full_nb_grid = {'stopwords': ['sksw', 'nltksw', 'addsw', 'allsw', 'sw_none'],
                'lemm': [None, 'wordnet'],
                'stem': [None, 'snowball', 'porter']}

combs = itertools.product(*(full_nb_grid[Name] for Name in full_nb_grid))


def print_combs(data=combs):
    return ['{}, {}, {}'.format(item[0], item[1], item[2]) for item in data]


combs_list = print_combs()


combs_dict = {'None': None, 'sksw': sksw, 'nltksw': nltksw, 'addsw': addsw,
              'allsw': allsw(),'sw_none': [], 'wordnet': wordnet,
              'snowball': snowball, 'porter': porter}


cv_pipeline = Pipeline([
    ('convert_lyrics', CountVectorizer()),
    ('tf-idf', TfidfTransformer()),
    ('naive_bayes', MultinomialNB())
])


def lyrics_gridsearch(full_dataset, feature_list=combs_list):
    for item in feature_list:
        sw = combs_dict[item.split(', ')[0]]
        lm = combs_dict[item.split(', ')[1]]
        stm = combs_dict[item.split(', ')[2]]

        clean_dataset, clean_lyrics = clean_full_dataset(
            full_dataset, sw, lm, stm)
        X = clean_lyrics
        y = clean_dataset['Test_Artist']

        nb_best_params, nb_best_model = gridsearch_with_output(cv_pipeline,
                                                               feats_grid,
                                                               X, y)
        print("\nComparing model with gridsearch params to initial model on Test set.")
        print(
            f"Stopwords: {item.split(', ')[0]}, Lemm: {item.split(', ')[1]}, Stem: {item.split(', ')[2]}\n")
        lyrics_pipeline = set_pipeline(X, y)
        display_default_and_gsearch_model_results(
            lyrics_pipeline, nb_best_model, X, y)
        print('-------------------------------------------------------\n')


if __name__ == '__main__':
    lyrics_gridsearch(full_dataset, combs_list)
