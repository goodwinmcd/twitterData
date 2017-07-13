import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    output = open('finalOutput2.txt', 'w')
    scores = {}
    aveScores = []
    terms = []
    tweets = []
    for line in sent_file:
      term, score = line.split("\t")
      terms.append(term)
      scores[term] = int(score)
    

    for line in tweet_file:
      tweets.append(json.loads(line))

    for each in tweets:
      score = 0
      each['text'] = each['text'].encode('ascii', 'ignore')
      for t in terms:
        if t in each['text']:
	  score = score + int(scores[t])
	  aveScores.append(score)
    total = 0
    for each in aveScores:
      total = total + each
    average = float(total)/len(aveScores)
    print average

if __name__ == '__main__':
    main()
