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

url = "http://api.linkedin.com/v1/people/~?format=json"

consumer = oauth.Consumer(
     key="19u63nenrggi",
     secret="wVS2M3qJxoOMcSMW")
     
token = oauth.Token(
     key="a6a437de-7682-4a62-9e61-ecf3a00a7d90", 
     secret="033e0103-1850-4c74-a62f-4f03ca222543")

client = oauth.Client(consumer, token)

resp, content = client.request(url)
# print resp
# print content

try:
    content=json.loads(content)
    print content['firstName'],content['lastName']
except:
    None
    
print "\n********A basic user profile call with field selectors going into a subresource********"
api_url = "http://api.linkedin.com/v1/people/~:(first-name,last-name,positions:(company:(name)))%s" % '?format=json'
response = make_request(client,api_url)
print response
    
# Get network updates that are shares or connection updates
print "\n********GET network updates that are CONN and SHAR********"
response = make_request(client,"http://api.linkedin.com/v1/people/~/network/updates?type=SHAR&type=CONN&format=json")
print response

# People search using facets and encoding input parameters
print "\n********People Search using facets and encoding input parameters********"
response = make_request(client,"http://api.linkedin.com/v1/people-search:(people:(first-name,last-name,headline))?title=D%C3%A9veloppeur&format=json")
print response

# the tokens have not expired even after 24 hours.