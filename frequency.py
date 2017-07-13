import sys
import json

tweet_file = open('output.txt')
tweets = []
frequency = {}

for line in tweet_file:
  tweets.append(json.loads(line))

for each in tweets:
  if 'text' in each and 'lang' in each:                     #make sure that the tweet is not deleted
    if each['lang'] == 'en':                                #make sure that the tweet is in english
      each['text'] = each['text'].encode('ascii', 'ignore') #Some tweets include symbols that throw conversion errors.  If it can't be 
                                                             #ascii decoded then ignore it
      allTermsInTweet = each['text'].split(' ')             #seperate all words
      for word in allTermsInTweet:
        word = word.translate(None, '!#*&^%.?"')
	if word in frequency:
	  frequency[word] = frequency[word] + 1
	else:
	  frequency[word] = 1

for each in frequency:
  print each + ' ' + str((float(frequency[each])/len(frequency)) * 10000)
