import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    undefinedTermsFile = open('undefinedTerms.txt', 'w')
    output = open('finalOutput.txt', 'w')
    tweets = []
    terms = []
    scores = {}
    undefinedTerms = {}
    for line in sent_file:
      term, score = line.split("\t")
      terms.append(term)
      scores[term] = int(score)
    
    for line in tweet_file:
      tweets.append(json.loads(line))

    for each in tweets:
      wordCount = 1
      score = 0
      undefinedTermsTemp = {}
      if 'text' in each and 'lang' in each:			#make sure that the tweet is not deleted
        if each['lang'] == 'en':				#make sure that the tweet is in english
	  each['text'] = each['text'].encode('ascii', 'ignore') #Some tweets include symbols that throw conversion errors.  If it can't be 
	  							#ascii decoded then ignore it
          allTermsInTweet = each['text'].split(' ')		#seperate all words
	  for word in allTermsInTweet:
	    word = word.translate(None, '!#*&^%.?"')		#remove punctuations
	    if word not in terms:				#if the word is not in the list of terms then save it in dictionary that is only not empty
	      undefinedTermsTemp[word] = 0			#during this loop
	    else:
	      wordCount = wordCount + 1
              score = score + scores[word]			#else get the score of the individual word
	  for word in undefinedTermsTemp:			
	    if word in undefinedTerms: 					#If the word was previously encountered then average previous score with new score
	      undefinedTerms[word] = (undefinedTerms[word] + score)/2
	    else: 
	      undefinedTerms[word] = float(score)/wordCount	#Only devide by the ammount of words that already had a sentiment value
      output.write(str(score) + '\n')
    for each in undefinedTerms:
      if undefinedTerms[each] != 0:
        print (each + ' ' + str(undefinedTerms[each]))
      undefinedTermsFile.write(each + ' ' + str(undefinedTerms[each]) + '\n')

if __name__ == '__main__':
    main()
