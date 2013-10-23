'''
Created on Oct 18, 2013

@author: Yuan-Fang
'''

import oauth2 as oauth
import httplib2
import time, os, json

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

# Fill the keys and secrets you retrieved after registering your app
consumer_key      =   '19u63nenrggi'
consumer_secret  =   'wVS2M3qJxoOMcSMW'
user_token           =   'c114a787-d0f3-4393-8c6a-62fa92f6f243'
user_secret          =   'df902b65-86dc-4fa3-aaf3-baf55ae5199c'

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)

client = oauth.Client(consumer, access_token)
 
# Make call to LinkedIn to retrieve your own profile
resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")

print content
print type(content)

try:
    content=json.loads(content)
except:
    print "error"
    
print content.keys()

# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
# resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")


