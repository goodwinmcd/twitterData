#! /bin/bash

python2 twitterstream2.py > output2.txt
python2 tweet_sentiment2.py AFINN-111.txt output2.txt >> averages.txt

