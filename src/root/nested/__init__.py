from Bio import Entrez, Medline
from BeautifulSoup import BeautifulSoup as bs4

Entrez.email='yffu@umich.edu'

handle= Entrez.egquery(term="Kai Zheng")

record= Entrez.read(handle)

for row in record['eGQueryResult']:
    if row["DbName"]=="pubmed":
        print row["Count"]

handle=Entrez.esearch(db="pubmed", term="Kai Zheng", retmax=200,usehistory="y")
record=Entrez.read(handle)
handle.close()
idlist=record["IdList"]
webenv=record["WebEnv"]
query=record["QueryKey"]

papers=Entrez.efetch(db="pubmed", query_key=query, rettype="abstract", WebEnv=webenv, retmode="html", retmax=50)

for pap in papers:
    try:
        pap=bs4(pap)
        print type(pap).prettify()
    except:
        print 'Nope'
#     print "title:", record.get("TI")
#     print "authors:", record.get("AU")
#     print "source:", record.get("SO")
    
# hand2=Entrez.efetch(db="pubmed", id=idlist, rettype='abstract', retmode="text", retmax=50)
# records= Medline.parse(handle)

# for record in records:
#     print records
#     print "title:", record.get("TI","?")
#     print "authors:", record.get("AU","?")
#     print "source:", record.get("SO","?")