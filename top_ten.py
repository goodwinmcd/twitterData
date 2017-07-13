import sys
import json
import collections
from collections import Counter

def main():
      tweet_file = open('output.txt')
      tweets = []
      hashs = {}
      for line in tweet_file:
        tweets.append(json.loads(line))
      for each in tweets:
        if 'text' in each and 'lang' in each and 'entities' in each:       #make sure that the tweet is not deleted
          if each['lang'] == 'en':                                #make sure that the tweet is in english
            each['text'] = each['text'].encode('ascii', 'ignore') #Some tweets include symbols that throw conversion errors.  If it can't be
                                                                #ascii decoded then ignore it
            hashtags = each['entities']['hashtags']
	    for h in hashtags:
              if h['text'] in hashs: hashs[h['text']] = hashs[h['text']] + 1
	      else: hashs[h['text']] = 1
      count = Counter(hashs)
      d = dict(sorted(count.most_common(10)))
      for each in d:
        print each + ' ' + str(d[each])
#      for each in hashs:
#        print each + ' ' + str(hashs[each])

if __name__ == '__main__':
    main()
