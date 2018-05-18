#!/usr/bin/python
# coding: utf-8

import requests
import lxml
from mysolr import Solr
from apesmit import Sitemap #library for writing sitemap XML
import time
import sys

'''Currently writing only <50,000 objects.  Will need to read response.result.numFound and write new files if need be.'''

'''Sitemap index:
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<sitemap>
   <loc>http://digital.library.wayne.edu/sitemaps/sitemap1.xml</loc>
   <lastmod>2004-10-01T18:23:17+00:00</lastmod>
</sitemap>
</sitemapindex>
'''

def getSingleObjects(id_list, start):		
	tcount = 0	
	solr = Solr('http://localhost:8080/solr4/fedobjs')
	query = {'q' : 'rels_isDiscoverable:True', 'fl' : 'id', 'rows' : 50000, 'start' : 0}
	response = solr.search(**query)
	print "Num Results:",response.total_results
	for each in response.documents:
		# print "adding:",each['id']
		id_list.append(each['id'])		
		tcount+=1
	print "Writing",tcount,"results..."
	writeSitemapXML(id_list)


def writeSitemapXML(id_list):
	sm = Sitemap(changefreq='weekly')
	for object_id in id_list:
		urladd = "https://digital.library.wayne.edu/item/{object_id}".format(object_id=object_id)
		sm.add(
			urladd,
			lastmod="today"
		)
	filename = "/var/www/wsuls/digitalcollections/public/sitemaps/sitemap_https.xml"
	fhand = open(filename,"w")
	sm.write(fhand)
	fhand.close()


def main():
	stime = time.time()
	id_list = []
	getSingleObjects(id_list,0)
	etime = time.time()
	print "Time Elapsed:",etime-stime


if __name__ == "__main__":
	#get args

	main()
