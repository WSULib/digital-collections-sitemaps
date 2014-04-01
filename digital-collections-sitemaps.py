#!/usr/bin/python
# coding: utf-8

import requests
import lxml
import sunburnt
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
	smCount = 1
	tcount = 0	
	si = sunburnt.SolrInterface("http://localhost:8080/solr4/fedobjs/")	
	response = si.query(id="wayne*").query(rels_isDiscoverable="true").field_limit("id").paginate(start=start,rows=50000).execute()	
	print "Num Results:",response.result.numFound
	for each in response:
		# print "adding:",each['id']
		id_list.append(each['id'])		
		tcount+=1
	print "Writing",tcount,"results..."
	writeSitemapXML(id_list, smCount)


def writeSitemapXML(id_list, smCount):
	sm = Sitemap(changefreq='weekly')
	for object_id in id_list:
		urladd = "http://digital.library.wayne.edu/digitalcollections/item?id={object_id}".format(object_id=object_id)
		sm.add(
			urladd,
			lastmod="today"
		)
	filename = "/var/www/wsuls/digitalcollections/sitemaps/sitemap{smCount}.xml".format(smCount=smCount)
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
