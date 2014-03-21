#!/usr/bin/python
# coding: utf-8

import requests
import lxml
import sunburnt


# example sunburnt code
'''	
si = sunburnt.SolrInterface("http://localhost:8080/solr4/users/")	
response = si.query(user_username=username).execute()
recordedHash = response[0]['user_hash'][0]
print "Provided:",providedHash
print "Recorded:",recordedHash
if providedHash == recordedHash:
	print "Credentials look good, proceeding."
	# delete doc
	PID = getParams['PID'][0]
	si.delete(username+"_"+PID)
	si.commit()

	# return response
	returnDict['username'] = username
	returnDict['favorite_removed'] = PID
	return json.dumps(returnDict)

else:
	print "Credentials don't match."
	returnDict['status'] = "Credentials don't match."
	return json.dumps(returnDict)
'''

# desired output
'''
** Sitemap **

<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" 
	<url> 
		<loc>http://digital.library.wayne.edu/digitalcollections/item?id=wayne:CFAIEB02b001</loc> 
		<lastmod>YYYY-MM-DDThh:mmTZD</lastmod>
	</url>
</urlset>

** Index of Sitemaps **

<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
	<sitemap>
		<loc>http://www.example.com/sitemap1.xml.gz</loc>
		<lastmod>2004-10-01T18:23:17+00:00</lastmod>
	</sitemap>
	<sitemap>
		<loc>http://www.example.com/sitemap2.xml.gz</loc>
		<lastmod>2005-01-01</lastmod>
	</sitemap>
</sitemapindex>
'''


def getSingleObjects():
	doc_dict = {}
	si = sunburnt.SolrInterface("http://localhost:8080/solr4/fedobjs/")	
	# with 50,000, there is an error. It's proably in one record, but how do we do this with exceptions?
	response = si.query(id="wayne*").paginate(start=0,rows=50000).execute()
	for each in response:
		do stuff, push to doc_dict


def writeSitemapXML(doc_dict):
	pass