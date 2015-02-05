#!/usr/bin/env python2

PATH = '/home/mohamed/wallpapers'
PAGES = 5

def screenRes() :
	import Tkinter
	return { 'height' : Tkinter.Tk().winfo_screenheight(),
	         'width' : Tkinter.Tk().winfo_screenwidth() }

def save(url, filename) :
	import urllib
	from os import path
	sv = path.join(PATH, filename + '.' + 'jpg')
	urllib.urlretrieve(url, sv)

def crawl(height, width, page) :
	import urllib2
	from bs4 import BeautifulSoup
	import re
	url = 'http://alpha.wallhaven.cc/search?categories=111&purity=100&resolutions=%sx%s&sorting=random&order=desc&page=%s' % (width, height, page)
	print url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html, 'html')
	ss = soup.findAll('a', {'class' : 'preview' })
	for s in ss :
		filename = re.search(r'\d+', s['href']).group(0)
		url = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg' % filename
		#print url
		save(url, filename)

for i in range(1, PAGES+1) :
	dic = screenRes()
	crawl(dic['height'], dic['width'], i)