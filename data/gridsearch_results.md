## First run

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 12000    | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: None

Gridsearched model acc: 0.910 | pre: 0.860 | rec = 0.979 | f1 = 0.916
     Default model acc: 0.910 | pre: 0.858 | rec = 0.982 | f1 = 0.916
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.823 | pre: 0.786 | rec = 0.888 | f1 = 0.834
     Default model acc: 0.870 | pre: 0.803 | rec = 0.981 | f1 = 0.883
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.825 | pre: 0.785 | rec = 0.895 | f1 = 0.836
     Default model acc: 0.872 | pre: 0.805 | rec = 0.982 | f1 = 0.885
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    6.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.824 | pre: 0.783 | rec = 0.896 | f1 = 0.836
     Default model acc: 0.886 | pre: 0.824 | rec = 0.981 | f1 = 0.896
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.824 | pre: 0.789 | rec = 0.885 | f1 = 0.834
     Default model acc: 0.870 | pre: 0.803 | rec = 0.982 | f1 = 0.883
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.826 | pre: 0.788 | rec = 0.891 | f1 = 0.837
     Default model acc: 0.873 | pre: 0.805 | rec = 0.984 | f1 = 0.885
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: None

Gridsearched model acc: 0.839 | pre: 0.806 | rec = 0.891 | f1 = 0.847
     Default model acc: 0.897 | pre: 0.837 | rec = 0.987 | f1 = 0.906
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.814 | pre: 0.771 | rec = 0.891 | f1 = 0.827
     Default model acc: 0.861 | pre: 0.789 | rec = 0.985 | f1 = 0.876
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.891 | pre: 0.840 | rec = 0.964 | f1 = 0.898
     Default model acc: 0.860 | pre: 0.788 | rec = 0.984 | f1 = 0.875
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   13.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.904 | pre: 0.857 | rec = 0.969 | f1 = 0.910
     Default model acc: 0.877 | pre: 0.810 | rec = 0.985 | f1 = 0.889
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.817 | pre: 0.776 | rec = 0.891 | f1 = 0.830
     Default model acc: 0.861 | pre: 0.790 | rec = 0.984 | f1 = 0.877
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: nltksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.813 | pre: 0.773 | rec = 0.887 | f1 = 0.826
     Default model acc: 0.862 | pre: 0.791 | rec = 0.984 | f1 = 0.877
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: None

Gridsearched model acc: 0.835 | pre: 0.782 | rec = 0.927 | f1 = 0.849
     Default model acc: 0.823 | pre: 0.740 | rec = 0.994 | f1 = 0.848
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   19.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.801 | pre: 0.753 | rec = 0.896 | f1 = 0.819
     Default model acc: 0.798 | pre: 0.715 | rec = 0.992 | f1 = 0.831
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.804 | pre: 0.755 | rec = 0.900 | f1 = 0.821
     Default model acc: 0.803 | pre: 0.720 | rec = 0.992 | f1 = 0.834
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   21.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.831 | pre: 0.782 | rec = 0.917 | f1 = 0.844
     Default model acc: 0.807 | pre: 0.724 | rec = 0.994 | f1 = 0.837
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   20.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.806 | pre: 0.758 | rec = 0.898 | f1 = 0.822
     Default model acc: 0.805 | pre: 0.722 | rec = 0.992 | f1 = 0.835
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: addsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.808 | pre: 0.761 | rec = 0.898 | f1 = 0.824
     Default model acc: 0.807 | pre: 0.724 | rec = 0.992 | f1 = 0.837
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: None

Gridsearched model acc: 0.818 | pre: 0.780 | rec = 0.887 | f1 = 0.830
     Default model acc: 0.915 | pre: 0.866 | rec = 0.982 | f1 = 0.920
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    7.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.812 | pre: 0.771 | rec = 0.888 | f1 = 0.825
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.810 | pre: 0.767 | rec = 0.890 | f1 = 0.824
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   17.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.821 | pre: 0.778 | rec = 0.898 | f1 = 0.834
     Default model acc: 0.895 | pre: 0.836 | rec = 0.984 | f1 = 0.904
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.814 | pre: 0.774 | rec = 0.887 | f1 = 0.826
     Default model acc: 0.881 | pre: 0.819 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: allsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.897 | pre: 0.853 | rec = 0.959 | f1 = 0.903
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   25.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: None

Gridsearched model acc: 0.823 | pre: 0.775 | rec = 0.911 | f1 = 0.838
     Default model acc: 0.814 | pre: 0.731 | rec = 0.994 | f1 = 0.842
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: snowball

Gridsearched model acc: 0.805 | pre: 0.763 | rec = 0.885 | f1 = 0.819
     Default model acc: 0.794 | pre: 0.711 | rec = 0.992 | f1 = 0.828
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: None, Stem: porter

Gridsearched model acc: 0.828 | pre: 0.784 | rec = 0.906 | f1 = 0.841
     Default model acc: 0.796 | pre: 0.712 | rec = 0.992 | f1 = 0.829
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.826 | pre: 0.779 | rec = 0.909 | f1 = 0.839
     Default model acc: 0.803 | pre: 0.720 | rec = 0.992 | f1 = 0.834
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   17.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.807 | pre: 0.764 | rec = 0.888 | f1 = 0.822
     Default model acc: 0.798 | pre: 0.715 | rec = 0.992 | f1 = 0.831
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   28.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.
Stopwords: sw_none, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.830 | pre: 0.785 | rec = 0.908 | f1 = 0.842
     Default model acc: 0.799 | pre: 0.716 | rec = 0.992 | f1 = 0.832
-------------------------------------------------------

# Second run

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   18.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 12000    | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: None

Gridsearched model acc: 0.910 | pre: 0.860 | rec = 0.979 | f1 = 0.916
     Default model acc: 0.910 | pre: 0.858 | rec = 0.982 | f1 = 0.916
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.823 | pre: 0.786 | rec = 0.888 | f1 = 0.834
     Default model acc: 0.870 | pre: 0.803 | rec = 0.981 | f1 = 0.883
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.825 | pre: 0.785 | rec = 0.895 | f1 = 0.836
     Default model acc: 0.872 | pre: 0.805 | rec = 0.982 | f1 = 0.885
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.9s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.824 | pre: 0.783 | rec = 0.896 | f1 = 0.836
     Default model acc: 0.886 | pre: 0.824 | rec = 0.981 | f1 = 0.896
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.824 | pre: 0.789 | rec = 0.885 | f1 = 0.834
     Default model acc: 0.870 | pre: 0.803 | rec = 0.982 | f1 = 0.883
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   14.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.826 | pre: 0.788 | rec = 0.891 | f1 = 0.837
     Default model acc: 0.873 | pre: 0.805 | rec = 0.984 | f1 = 0.885
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.3s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: None

Gridsearched model acc: 0.839 | pre: 0.806 | rec = 0.891 | f1 = 0.847
     Default model acc: 0.897 | pre: 0.837 | rec = 0.987 | f1 = 0.906
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.814 | pre: 0.771 | rec = 0.891 | f1 = 0.827
     Default model acc: 0.861 | pre: 0.789 | rec = 0.985 | f1 = 0.876
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.5s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: None, Stem: porter

Gridsearched model acc: 0.891 | pre: 0.840 | rec = 0.964 | f1 = 0.898
     Default model acc: 0.860 | pre: 0.788 | rec = 0.984 | f1 = 0.875
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.904 | pre: 0.857 | rec = 0.969 | f1 = 0.910
     Default model acc: 0.877 | pre: 0.810 | rec = 0.985 | f1 = 0.889
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.817 | pre: 0.776 | rec = 0.891 | f1 = 0.830
     Default model acc: 0.861 | pre: 0.790 | rec = 0.984 | f1 = 0.877
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   12.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: nltksw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.813 | pre: 0.773 | rec = 0.887 | f1 = 0.826
     Default model acc: 0.862 | pre: 0.791 | rec = 0.984 | f1 = 0.877
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   16.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: None

Gridsearched model acc: 0.835 | pre: 0.782 | rec = 0.927 | f1 = 0.849
     Default model acc: 0.823 | pre: 0.740 | rec = 0.994 | f1 = 0.848
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   19.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.801 | pre: 0.753 | rec = 0.896 | f1 = 0.819
     Default model acc: 0.798 | pre: 0.715 | rec = 0.992 | f1 = 0.831
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.0s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.804 | pre: 0.755 | rec = 0.900 | f1 = 0.821
     Default model acc: 0.803 | pre: 0.720 | rec = 0.992 | f1 = 0.834
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.831 | pre: 0.782 | rec = 0.917 | f1 = 0.844
     Default model acc: 0.807 | pre: 0.724 | rec = 0.994 | f1 = 0.837
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.806 | pre: 0.758 | rec = 0.898 | f1 = 0.822
     Default model acc: 0.805 | pre: 0.722 | rec = 0.992 | f1 = 0.835
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: addsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.808 | pre: 0.761 | rec = 0.898 | f1 = 0.824
     Default model acc: 0.807 | pre: 0.724 | rec = 0.992 | f1 = 0.837
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.6s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: None

Gridsearched model acc: 0.818 | pre: 0.780 | rec = 0.887 | f1 = 0.830
     Default model acc: 0.915 | pre: 0.866 | rec = 0.982 | f1 = 0.920
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   11.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: snowball

Gridsearched model acc: 0.812 | pre: 0.771 | rec = 0.888 | f1 = 0.825
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   10.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: None, Stem: porter

Gridsearched model acc: 0.810 | pre: 0.767 | rec = 0.890 | f1 = 0.824
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.8s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.821 | pre: 0.778 | rec = 0.898 | f1 = 0.834
     Default model acc: 0.895 | pre: 0.836 | rec = 0.984 | f1 = 0.904
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    9.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.814 | pre: 0.774 | rec = 0.887 | f1 = 0.826
     Default model acc: 0.881 | pre: 0.819 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:    8.7s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 5000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: allsw, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.897 | pre: 0.853 | rec = 0.959 | f1 = 0.903
     Default model acc: 0.880 | pre: 0.818 | rec = 0.977 | f1 = 0.891
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   19.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: None

Gridsearched model acc: 0.823 | pre: 0.775 | rec = 0.911 | f1 = 0.838
     Default model acc: 0.814 | pre: 0.731 | rec = 0.994 | f1 = 0.842
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   15.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: snowball

Gridsearched model acc: 0.805 | pre: 0.763 | rec = 0.885 | f1 = 0.819
     Default model acc: 0.794 | pre: 0.711 | rec = 0.992 | f1 = 0.828
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   23.1s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: None, Stem: porter

Gridsearched model acc: 0.828 | pre: 0.784 | rec = 0.906 | f1 = 0.841
     Default model acc: 0.796 | pre: 0.712 | rec = 0.992 | f1 = 0.829
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   18.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: None

Gridsearched model acc: 0.826 | pre: 0.779 | rec = 0.909 | f1 = 0.839
     Default model acc: 0.803 | pre: 0.720 | rec = 0.992 | f1 = 0.834
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   18.4s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 500      | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: snowball

Gridsearched model acc: 0.807 | pre: 0.764 | rec = 0.888 | f1 = 0.822
     Default model acc: 0.798 | pre: 0.715 | rec = 0.992 | f1 = 0.831
-------------------------------------------------------

Fitting 4 folds for each of 8 candidates, totalling 32 fits
[Parallel(n_jobs=-1)]: Done  32 out of  32 | elapsed:   19.2s finished

Result of gridsearch:
Parameter            | Optimal  | Gridsearch values
-------------------------------------------------------
convert_lyrics__max_features | 1000     | [None, 50, 100, 500, 1000, 5000, 10000, 12000]

Comparing model with gridsearch params to initial model on Test set.

Stopwords: sw_none, Lemm: wordnet, Stem: porter

Gridsearched model acc: 0.830 | pre: 0.785 | rec = 0.908 | f1 = 0.842
     Default model acc: 0.799 | pre: 0.716 | rec = 0.992 | f1 = 0.832
-------------------------------------------------------
