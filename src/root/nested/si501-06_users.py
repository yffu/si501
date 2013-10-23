'''
Created on Oct 18, 2013

@author: Yuan-Fang
'''
import oauth2 as oauth
import time, json

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
def make_request(c, u):
    try:
        resp, content=c.request(u)
        return json.loads(content)
    except:
        print "not right"
        return None

# Access Token:
oauth_token        = 'a6a437de-7682-4a62-9e61-ecf3a00a7d90'
oauth_token_secret = '033e0103-1850-4c74-a62f-4f03ca222543'

url = "http://api.linkedin.com/v1/people/~?format=json"

consumer = oauth.Consumer(
     key="19u63nenrggi",
     secret="wVS2M3qJxoOMcSMW")
     
token = oauth.Token(
     key="23890760-9ad9-486c-83bc-86cbd624a476", 
     secret="3a25477f-d963-4dd8-b6b9-b5b7ceb8563b")


client = oauth.Client(consumer, token)

resp, content = client.request(url)
# print resp
# print content

try:
    content=json.loads(content)
    print content['firstName'],content['lastName']
except:
    None
    
# Simple profile call
print "\n********A basic user profile call********"
response = make_request(client,"http://api.linkedin.com/v1/people/~%s" % '?format=json')
print response

# Simple connections call
print "\n********Get the connections********"
response = make_request(client,"http://api.linkedin.com/v1/people/~/connections%s&%s" % ('?format=json', 'count=10'))
print response
print type(response)

# using field selectors

print "\n********A basic user profile call with field selectors********"
api_url = "http://api.linkedin.com/v1/people/~:(first-name,last-name,positions)%s" % '?format=json'
response = make_request(client,api_url)
print response

# return only the company names

print "\n********A basic user profile call with field selectors going into a subresource********"
api_url = "http://api.linkedin.com/v1/people/~:(first-name,last-name,positions:(company:(name)))%s" % '?format=json'
response = make_request(client,api_url)
print response

