#-*- coding: utf-8 -*-

'''
Created on Oct 11, 2013

@author: Yuan-Fang
'''
import json
import urllib

api_key = open(".freebase_api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/topic'
topic_id = '/m/0d6lp'
params = {
  'key': api_key,
  'filter': 'suggest'
}
url = service_url + topic_id + '?' + urllib.urlencode(params)
topic = json.loads(urllib.urlopen(url).read())

print json.dumps(topic, sort_keys=True, indent=4, separators=(',', ': '))