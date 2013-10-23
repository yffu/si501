'''
Created on Oct 18, 2013

@author: Yuan-Fang
'''
import urllib2, time, urlparse
from setuptools import setup
import oauth2 as oauth

# referenced from http://answers.oreilly.com/topic/1381-how-to-use-three-legged-oauth/

# the three legged oauth

# 1. client requests server for consumer key and consumer secret

# 2. client uses consumer key to get request token and secret

# 3. client directs user to the server to get permission, to let the client get the user resources. User give an authenticated request token.

# 4. client requests server to provide access token and secret, so client can access user information from server

# 5. when making request to access protected resource, client includes authorization header with:

# consumer key; access token; signature method and signature; timestamp; nounce; and optionally the version of Oauth protocol

# and the two legged oauth

# typical client server interaction, without participation of the user. 

# only involves consumer key and secret, with access tokens being blank

url='https://www.linkedin.com/uas/oauth2/authorization'

ckey='19u63nenrggi'

csecret='wVS2M3qJxoOMcSMW'


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

# we are the consumer/client

# a. Generate Authorization Code by redirecting user to LinkedIn's authorization dialog

rq_auth_code='https://www.linkedin.com/uas/oauth2/authorization?response_type=code \
                                           &client_id=YOUR_API_KEY \
                                           &scope=SCOPE \
                                           &state=STATE\
                                           &redirect_uri=YOUR_REDIRECT_URI'

# Upon successful authorization, the redirected URL should look like:

redirected='YOUR_REDIRECT_URI/?code=AUTHORIZATION_CODE&state=STATE'

# b. Request Access Token by exchanging the authorization_code for it

rq_acc_tok='https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code\
                                           &code=AUTHORIZATION_CODE\
                                           &redirect_uri=YOUR_REDIRECT_URI\
                                           &client_id=YOUR_API_KEY\
                                           &client_secret=YOUR_SECRET_KEY'
                                           
# The response will be a JSON object:

# {"expires_in":5184000,"access_token":"AQXdSP_W41_UPs5ioT_t8HESyODB4FqbkJ8LrV_5mff4gPODzOYR"}


# Step 3. Make the API calls

api_call='https://api.linkedin.com/v1/people/~?oauth2_access_token=AQXdSP_W41_UPs5ioT_t8HESyODB4FqbkJ8LrV_5mff4gPODzOYR'

consumer=oauth.Consumer(ckey, csecret)

client=oauth.Client(consumer)

params={
        'type':'code',
        'client_id':'19u63nenrggi',
        'state':oauth.generate_nonce(), # creates a random string that identifies the caller and response
        'redirect':'http://www.google.com'
        }

# Set our token/key parameters
params['oauth_token'] = 'c114a787-d0f3-4393-8c6a-62fa92f6f243'
params['oauth_consumer_key'] = 'df902b65-86dc-4fa3-aaf3-baf55ae5199c'