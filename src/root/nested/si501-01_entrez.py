'''
Created on Oct 10, 2013

@author: Yuan-Fang
'''

def findintree(elem):
    for child in elem:
        if child.findall() is not None:
            return None

from Bio import Entrez, Medline
import csv, pymysql, urllib2 as urllib
from time import sleep
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

outhandle=open('researchers.csv', 'w')
csvhand=csv.writer(outhandle, delimiter='\t')

# the search method is sensitive: best to use author only, don't restrict too many fields

Entrez.email="yffu@umich.edu"
handle=Entrez.esearch(db="pubmed", term="julia adler-milstein[Author]", retmax=10, usehistory='y')
record=Entrez.read(handle)
web=record["WebEnv"]
query= record["QueryKey"]
idlist=list(record["IdList"])
 
handle.close()
count=0
for id in idlist:
    print id
    eget='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=%s&retmode=xml' % id
    tmp=urllib.urlopen(eget).read()
    tree=ET.parse(tmp)
    
    sleep(0.3)
# it is the parse that turns xml files into a dictionary

