import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    output = open('finalOutput.txt', 'w')
    scores = {}
    terms = []
    for line in sent_file:
      term, score = line.split("\t")
      terms.append(term)
      scores[term] = int(score)
    
    tweets = []
    for line in tweet_file:
      tweets.append(json.loads(line))

    for each in tweets:
      score = 0
      if 'text' in each and 'lang' in each:			#make sure that the tweet is not deleted
        if each['lang'] == 'en':				#make sure that the tweet is in english
	  each['text'] = each['text'].encode('ascii', 'ignore') #Some tweets include symbols that throw conversion errors.  If it can't be 
	  							#ascii decoded then ignore it
	  for t in terms:					#check if a tweet contains any of the terms that have sentiment scores
            if t in each['text']:
              score = score + scores[t]
      output.write(str(score) + '\n')

if __name__ == '__main__':
    main()
