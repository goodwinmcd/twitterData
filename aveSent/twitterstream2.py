import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "yBYiyHd5FYPbEblAjgyTUtn6V"
api_secret = "o7B25J7BMRVpliZje84SHKJqiQSsK4SSOdoLIp4JweuPhsVnqE"
access_token_key = "353490143-3maFL5n8QVNUckqOXOKi9sFPUCSvmo9s2icmkqBB"
access_token_secret = "vqGMx9WBGJJYpBmHm9ToF3f3gaYXOm2JmFyWmBz30EQkj"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json?"
  parameters = ['en']
  response = twitterreq(url, "GET", parameters)
  i = 0
  for line in response:
    line = (line.strip())
    jLine = json.loads(line)
    if 'text' in jLine:
      print line
      i = i + 1
    if i > 1000: break

if __name__ == '__main__':
  fetchsamples()
