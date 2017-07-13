Based off assignment 1 here:  https://github.com/uwescience/datasci_course_materials/tree/master/assignment1

AFINN-111.txt contains a list of terms with a corresponding sentiment value

twitterstream.py streams live twitter feed.  I saved the feed to output.txt with command 'twitterstream.py > output.txt'.  It contains approximately 3 min of twitter stream

tweet_sentiment.py uses AFINN-111.txt and output.txt to assign a sentiment value to all the tweets that were collected.

term_sentiment.py assigns sentiment values to words that are not in AFINN-111.txt.  It is done using the sentiment values of the other words in the tweet

frequency.py counts the frequency of all terms in output.txt.  It is found with (# of times term appears in file)/(# of all terms in file)

top_ten.py counts the number of time a hashtag appears in the file and then outputs the top 10 most occuring ones

aveSent takes the average sentiment value of all tweets and saves it to a file.  I setup crontab to run tweeterstream2.py followed by tweet_sentiment2.py every 5 min so that I could plot it on a graph.  
