## First run

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 12000    | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: None

Gridsearched model acc: 0.903 | pre: 0.840 | rec = 0.989 | f1 = 0.908
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.774 | pre: 0.716 | rec = 0.883 | f1 = 0.791
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.760 | pre: 0.702 | rec = 0.878 | f1 = 0.780
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.806 | pre: 0.757 | rec = 0.883 | f1 = 0.815
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.776 | pre: 0.719 | rec = 0.883 | f1 = 0.793
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.763 | pre: 0.705 | rec = 0.878 | f1 = 0.782
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: None

Gridsearched model acc: 0.838 | pre: 0.800 | rec = 0.889 | f1 = 0.842
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.763 | pre: 0.709 | rec = 0.867 | f1 = 0.780
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.830 | pre: 0.760 | rec = 0.950 | f1 = 0.844
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.908 | pre: 0.858 | rec = 0.972 | f1 = 0.911
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.760 | pre: 0.710 | rec = 0.856 | f1 = 0.776
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.747 | pre: 0.694 | rec = 0.856 | f1 = 0.766
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   17.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: None

Gridsearched model acc: 0.846 | pre: 0.844 | rec = 0.839 | f1 = 0.841
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.776 | pre: 0.737 | rec = 0.839 | f1 = 0.784
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.752 | pre: 0.710 | rec = 0.828 | f1 = 0.764
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.825 | pre: 0.818 | rec = 0.822 | f1 = 0.820
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.774 | pre: 0.735 | rec = 0.833 | f1 = 0.781
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.760 | pre: 0.716 | rec = 0.839 | f1 = 0.772
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: None

Gridsearched model acc: 0.798 | pre: 0.740 | rec = 0.900 | f1 = 0.812
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.757 | pre: 0.696 | rec = 0.889 | f1 = 0.780
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.744 | pre: 0.678 | rec = 0.900 | f1 = 0.773
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.814 | pre: 0.753 | rec = 0.917 | f1 = 0.827
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.760 | pre: 0.699 | rec = 0.889 | f1 = 0.782
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.819 | pre: 0.747 | rec = 0.950 | f1 = 0.836
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: None

Gridsearched model acc: 0.841 | pre: 0.831 | rec = 0.844 | f1 = 0.837
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   18.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: snowball

Gridsearched model acc: 0.795 | pre: 0.765 | rec = 0.833 | f1 = 0.798
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: porter

Gridsearched model acc: 0.795 | pre: 0.774 | rec = 0.817 | f1 = 0.795
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.811 | pre: 0.809 | rec = 0.800 | f1 = 0.804
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.790 | pre: 0.763 | rec = 0.822 | f1 = 0.791
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.792 | pre: 0.772 | rec = 0.811 | f1 = 0.791
     Default model acc: 0.695 | pre: 0.622 | rec = 0.950 | f1 = 0.752
-------------------------------------------------------


Second run:
Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 12000    | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: None

Gridsearched model acc: 0.900 | pre: 0.840 | rec = 0.983 | f1 = 0.906
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.798 | pre: 0.745 | rec = 0.890 | f1 = 0.811
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.776 | pre: 0.725 | rec = 0.873 | f1 = 0.792
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.811 | pre: 0.779 | rec = 0.856 | f1 = 0.816
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.795 | pre: 0.746 | rec = 0.878 | f1 = 0.807
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.774 | pre: 0.724 | rec = 0.867 | f1 = 0.789
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: None

Gridsearched model acc: 0.838 | pre: 0.801 | rec = 0.890 | f1 = 0.843
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.779 | pre: 0.730 | rec = 0.867 | f1 = 0.793
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.827 | pre: 0.760 | rec = 0.945 | f1 = 0.842
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.898 | pre: 0.856 | rec = 0.950 | f1 = 0.901
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.784 | pre: 0.744 | rec = 0.851 | f1 = 0.794
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.768 | pre: 0.723 | rec = 0.851 | f1 = 0.782
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: None

Gridsearched model acc: 0.844 | pre: 0.851 | rec = 0.823 | f1 = 0.837
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   23.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.779 | pre: 0.754 | rec = 0.812 | f1 = 0.782
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   28.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.765 | pre: 0.735 | rec = 0.812 | f1 = 0.772
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.833 | pre: 0.848 | rec = 0.801 | f1 = 0.824
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   22.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.771 | pre: 0.750 | rec = 0.796 | f1 = 0.772
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   20.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.765 | pre: 0.737 | rec = 0.807 | f1 = 0.770
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: None

Gridsearched model acc: 0.814 | pre: 0.775 | rec = 0.873 | f1 = 0.821
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.782 | pre: 0.725 | rec = 0.890 | f1 = 0.799
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   18.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.771 | pre: 0.709 | rec = 0.901 | f1 = 0.793
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.811 | pre: 0.763 | rec = 0.890 | f1 = 0.821
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.792 | pre: 0.736 | rec = 0.895 | f1 = 0.808
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.825 | pre: 0.752 | rec = 0.956 | f1 = 0.842
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: None

Gridsearched model acc: 0.860 | pre: 0.882 | rec = 0.823 | f1 = 0.851
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: snowball

Gridsearched model acc: 0.787 | pre: 0.777 | rec = 0.790 | f1 = 0.784
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: porter

Gridsearched model acc: 0.806 | pre: 0.791 | rec = 0.818 | f1 = 0.804
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.825 | pre: 0.845 | rec = 0.785 | f1 = 0.814
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.792 | pre: 0.786 | rec = 0.790 | f1 = 0.788
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.795 | pre: 0.781 | rec = 0.807 | f1 = 0.793
     Default model acc: 0.658 | pre: 0.594 | rec = 0.939 | f1 = 0.728
-------------------------------------------------------

# Second run

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 12000    | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: None

Gridsearched model acc: 0.911 | pre: 0.849 | rec = 0.994 | f1 = 0.916
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.795 | pre: 0.729 | rec = 0.923 | f1 = 0.815
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.798 | pre: 0.730 | rec = 0.928 | f1 = 0.818
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.846 | pre: 0.798 | rec = 0.917 | f1 = 0.853
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.811 | pre: 0.749 | rec = 0.923 | f1 = 0.827
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    5.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.801 | pre: 0.738 | rec = 0.917 | f1 = 0.818
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: None

Gridsearched model acc: 0.852 | pre: 0.800 | rec = 0.928 | f1 = 0.859
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.774 | pre: 0.716 | rec = 0.890 | f1 = 0.793
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.876 | pre: 0.808 | rec = 0.978 | f1 = 0.885
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.933 | pre: 0.894 | rec = 0.978 | f1 = 0.934
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.782 | pre: 0.729 | rec = 0.878 | f1 = 0.797
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.776 | pre: 0.725 | rec = 0.873 | f1 = 0.792
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: None

Gridsearched model acc: 0.863 | pre: 0.853 | rec = 0.867 | f1 = 0.860
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.795 | pre: 0.764 | rec = 0.840 | f1 = 0.800
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.792 | pre: 0.760 | rec = 0.840 | f1 = 0.798
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.873 | pre: 0.872 | rec = 0.867 | f1 = 0.870
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.792 | pre: 0.763 | rec = 0.834 | f1 = 0.797
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.792 | pre: 0.760 | rec = 0.840 | f1 = 0.798
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: None

Gridsearched model acc: 0.819 | pre: 0.754 | rec = 0.934 | f1 = 0.835
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.784 | pre: 0.717 | rec = 0.923 | f1 = 0.807
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.765 | pre: 0.697 | rec = 0.917 | f1 = 0.792
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.830 | pre: 0.768 | rec = 0.934 | f1 = 0.843
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.784 | pre: 0.717 | rec = 0.923 | f1 = 0.807
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.876 | pre: 0.808 | rec = 0.978 | f1 = 0.885
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: None

Gridsearched model acc: 0.871 | pre: 0.859 | rec = 0.878 | f1 = 0.869
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: snowball

Gridsearched model acc: 0.809 | pre: 0.775 | rec = 0.856 | f1 = 0.814
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: porter

Gridsearched model acc: 0.841 | pre: 0.818 | rec = 0.867 | f1 = 0.842
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.876 | pre: 0.877 | rec = 0.867 | f1 = 0.872
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.811 | pre: 0.785 | rec = 0.845 | f1 = 0.814
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.836 | pre: 0.812 | rec = 0.862 | f1 = 0.836
     Default model acc: 0.677 | pre: 0.606 | rec = 0.967 | f1 = 0.745
-------------------------------------------------------
