# Binary Classification Using Bob Dylan Lyrics

## Background

After discovering the [Every song you have heard (almost)!](https://www.kaggle.com/artimous/every-song-you-have-heard-almost) song lyric dataset on Kaggle.com which includes over 500,000 song lyrics, I had a grandiose idea of determining which is a better predictor of song popularity: song lyrics or music composition. After being persuaded **(and rightfully so)** this project was a little ambitious for a first capstone, I was still curious if I could discover any meaning full data using song lyrics.

Even though our course has not covered Natural Language Processing, I was allowed to use this dataset for my capstone project as long as I understood that I would have to teach myself several NLP techniques over a short period of time. After spending a decent amount of time researching the subject, I decided to take the risk and proceed with this dataset.

### ~~Hot Dog/Not Hot Dog~~ Bob Dylan/ Not Bob Dylan

After deciding to use song lyrics for my capstone, I had to pivot and decide on a topic that used concepts we have learned about in class along with teaching myself some NLP techniques. After some contemplating, I remembered Bob Dylan is famous for not only writing his own music, but also writing many very famous songs that were made famous by other artists. Below is sample list of those songs. I knew he had written many songs but after some research, the total number of songs he is credited with writing is somewhere between 350 and 650 songs!!!. The Kaggle dataset has him listed as the artist for over 600 unique songs which gives me a below is sample list of those songs:

#### Songs Written by Bob Dylan made famous by other artists:
 * All Along the Watchtower - Jimi Hendrix (or DMB for some)
 * Mr. Tambourine Man - The Byrds
 * It Ain't Me Babe - The Turtles
 * Wagon Wheel - Old Crow Medicine Show (or Darius Rucker)
 * Love is Just a Four Letter Word - Joan Baez
 * The Mighty Quinn (Quinn the Eskimo) - Manfred Mann
 * Farewell or Fare Thee Well - most recently featured in the Coen Brother's Film "Inside Llewen Davis"

Eventually I decided the topic **"Bob Dylan/Not Bob Dylan"** with the goal of building a classification model to predict if a song was written in fact written by Bob Dylan.


## Process

### 1. Create a sample dataset:
The first step was to create a sample dataset to work with. I wrote a function that imported the entire dataset and then created a smaller dataset of every song labeled by the specified artist, Bob Dylan in this case. Next, the function adds a random sample of songs equal to the number of songs as the test artist.

For demonstration purposes, I made a two song dataset to show what the data looks like after each step of the process:

##### Demo Dataset:

| Band        |   Lyrics | Song                    |   Test_Artist |
|:------------|:---------|:------------------------|:--------------|
| Bob Dylan   | Go 'way from my window,\r\nLeave at your own c... | It Ain't Me Babe        | True |
| Rick Astley | We're no strangers to love\r\n\You know the rul... | Never Gonna Give You Up | False |

### 2. Clean the data:
The next step is to clean the strings in the dataset. There are different options for cleaning the data depending on your testing purposes. For my dataset, I initially cleaned the following items out of the dataset:
 * Remove Punctuation
 * Remove Stopwords (my default list was sklearn's built in list of stopwords)

##### Demo Dataset after cleaning:

| Band        |   Lyrics | Song                    |   Test_Artist |
|:------------|:---------|:------------------------|:--------------|
| Bob Dylan   | go way window leave chosen speed one want babe... | It Ain't Me Babe        | True |
| Rick Astley | strangers love know rules full commitments thi... | Never Gonna Give You Up | False |

### 3. Tokenize all words using bag of words method:
Next, you need take all of the remaining words in the dataset, also called the corpus, and convert them into a matrix. The matrix consists of one row for every song in the data set and one column for each word in the corpus.

##### Demo Dataset after tokenization:

||BD/NotBD|gonna|never|babe|give|want|
|:------------|:-----------|--------:|--------:|-------:|-------:|-------:|
|Bob Dylan|True|0|2|13|0|2|
|Rick Astley|False|12|10|0|9|2|

##### Top ten words in the demo corpus:

|    | word    |   count |
|---:|:--------|--------:|
|  1 | babe    |      13 |
|  2 | never   |      12 |
|  3 | gonna   |      12 |
|  4 | aint    |       9 |
|  5 | give    |       9 |
|  6 | someone |       7 |
|  7 | say     |       6 |
|  8 | know    |       5 |
|  9 | lookin  |       5 |
| 10 | ooh     |       4 |

##### Top ten words in the actual test dataset:

|    | word   |   count |
|---:|:-------|--------:|
|  1 | love   |    1470 |
|  2 | like   |    1435 |
|  3 | know   |    1390 |
|  4 | got    |    1180 |
|  5 | oh     |     986 |
|  6 | come   |     917 |
|  7 | time   |     852 |
|  8 | baby   |     800 |
|  9 | gonna  |     745 |
| 10 | say    |     738 |

### 4. Add weights to each word using the TF-IDF method:


###### Demo dataset after TF-IDF  
||BD/NotBD|gonna|never|babe|give|want|
|:------------|:-----------|-----------:|-----------:|-----------:|-----------:|----------:|
|Bob Dylan|True|0.00%|6.96%|63.54%|0.00%|6.96%|
|Rick Astley|False|57.95%|34.36%|0.00%|43.47%|6.87%|

##### Top ten words in the demo dataset:
|    | word    |    weight |
|---:|:--------|----------:|
|  1 | babe    | 0.3176   |
|  2 | gonna   | 0.2897  |
|  3 | aint    | 0.2199   |
|  4 | give    | 0.2173  |
|  5 | never   | 0.2065  |
|  6 | someone | 0.1710  |
|  7 | lookin  | 0.1221  |
|  8 | know    | 0.1207  |
|  9 | say     | 0.1037  |
| 10 | go      | 0.0977 |

###### Top ten weights in the actual test dataset:

|    | word   |    weight |
|---:|:-------|----------:|
|  1 | love   | 0.037% |
|  2 | know   | 0.029% |
|  3 | like   | 0.027% |
|  4 | got    | 0.024% |
|  5 | baby   | 0.024% |
|  6 | oh     | 0.023% |
|  7 | come   | 0.022% |
|  8 | time   | 0.022% |
|  9 | let    | 0.019% |
| 10 | say    | 0.019% |

### 5. Test the data using the Naive Bayes method:

**Given the song is Bob Dylan, what is the probability that we see that specific word?**

My initial results had the following results:

### Classification Statistics:

| Statistic   |   Result |
|:------------|---------:|
| Accuracy    |   0.7628 |
| Precision   |   0.7336 |
| Recall      |   0.8615 |
| F1-Score    |   0.7925 |


### Sparse Matrix:
| | |
|:------------|---------:|
| Shape of Sparse Matrix: | (1234, 14962) |
| Amount of Non-Zero occurences: | 79338 |
| Sparcity of Matrix: | 0.430 |


### Confusion Matrix

![confusion_matrix][1]

### ROC Plot:
![roc_plot][2]













[1]: images/confusion_matrix_orig.png
[2]: images/roc_plot_orig.png
