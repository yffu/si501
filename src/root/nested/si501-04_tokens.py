'''
Created on Oct 18, 2013

@author: Yuan-Fang
'''
import oauth2 as oauth
import urlparse 

'''
API Key:
19u63nenrggi
Secret Key:
wVS2M3qJxoOMcSMW
OAuth User Token:
c114a787-d0f3-4393-8c6a-62fa92f6f243
OAuth User Secret:
df902b65-86dc-4fa3-aaf3-baf55ae5199c
'''
  
consumer_key      =   '19u63nenrggi'
consumer_secret  =   'wVS2M3qJxoOMcSMW'
 
# initialize the oauth client
 
consumer = oauth.Consumer(consumer_key, consumer_secret)
 
client=oauth.Client(consumer) # no access token right now, since we are going to request one the consumer has only the key and SECRET
# while the client has access tokens

# get a request token

request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'

resp, content = client.request(request_token_url, 'POST')

if resp['status']!='200':
    raise Exception ("Invalid response %s." % resp['status'])

request_token=dict(urlparse.parse_qsl(content))

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
print 

# redirect the user to the provider

authorize_url= 'https://www.linkedin.com/uas/oauth/authenticate'
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

# pin is 53264

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

# this client now has authenticated token from the user, can now request access token from provider
 
resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))
 
print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print
print "You may now access protected resources using the access tokens above."
print