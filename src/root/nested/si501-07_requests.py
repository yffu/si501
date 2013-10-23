'''
Created on Oct 19, 2013

@author: Yuan-Fang
'''
import oauth2 as oauth
import time, json, urllib2

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
    
def error_handle(resp, content):
    if resp.status >= 200 and resp.status < 300:
        return content
    elif resp.status >= 500 and resp.status < 600:
        error_string = "Status:\n\tRuh Roh! An application error occured! HTTP 5XX response received."
        print resp.status + " : " + error_string
     
    else:
        status_codes = {403: "\n** Status:\n\tA 403 response was received. Usually this means you have reached a throttle limit.",
                        401: "\n** Status:\n\tA 401 response was received. Usually this means the OAuth signature was bad.",
                        405: "\n** Status:\n\tA 405 response was received. Usually this means you used the wrong HTTP method (GET when you should POST, etc).",
                        400: "\n** Status:\n\tA 400 response was received. Usually this means your request was formatted incorrectly or you added an unexpected parameter.",
                        404: "\n** Status:\n\tA 404 response was received. The resource was not found."}
        if resp.status in status_codes:
            print resp.status + " : " + status_codes[resp.status]
        else:
            print resp.status  + " : " + error_string

consumer = oauth.Consumer(
     key="19u63nenrggi",
     secret="wVS2M3qJxoOMcSMW")
     
token = oauth.Token(
     key="a6a437de-7682-4a62-9e61-ecf3a00a7d90", 
     secret="033e0103-1850-4c74-a62f-4f03ca222543")

client = oauth.Client(consumer, token)

print "\n********A basic user profile call and response dissected********"
api_url = "https://api.linkedin.com/v1/people/~";

resp,content = client.request(api_url)
 
print "\n** Response Headers:\n%s\n" % (resp)

print error_handle(resp, content)

