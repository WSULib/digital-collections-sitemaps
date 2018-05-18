#!/usr/bin/python
# coding: utf-8

import argparse
import requests
import lxml
from mysolr import Solr
from apesmit import Sitemap #library for writing sitemap XML
import time
import sys


def generate_sitemap(args):

	# init sitemap
	sm = Sitemap(changefreq='weekly')

	solr_handle = Solr('http://localhost:8080/solr4/fedobjs')
	query = {'q' : 'rels_isDiscoverable:True', 'fl' : 'id', 'start' : 0}

	# get solr cursor
	cursor = solr_handle.search_cursor(**query)

	# loop through and write to sitemap
	for chunk in cursor.fetch(100):
		for object_id in chunk.documents:
			urladd = "https://digital.library.wayne.edu/item/{object_id}".format(object_id=object_id)
			sm.add(
				urladd,
				lastmod="today"
			)

	# save to disk
	if args.output:
		filename = args.output
	else:
		filename = "/var/www/wsuls/digitalcollections/public/sitemaps/sitemap_https.xml"
	fhand = open(filename, "w")
	sm.write(fhand)
	fhand.close()
	print("sitemap created at %s, total time elapsed %s" % (filename, (time.time()-stime) ))


if __name__ == "__main__":
	
	# parse args
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--output', metavar='output', type=str, help='destination for sitemap, otherwise defaults to /var/www/wsuls/digitalcollections/public/sitemaps/sitemap_https.xml')
	args = parser.parse_args()

	stime = time.time()
	generate_sitemap(args)

