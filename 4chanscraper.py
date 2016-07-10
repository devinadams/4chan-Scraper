from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os


def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'lxml')

image_type = "image_name"
query = raw_input("Search? ")
url = "https://www.google.com/search?q=" + query + "&biw=1360&bih=645&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjl0cra7KPNAhUPIFIKHdqSCFcQ_AUIBigB#imgrc=nZ8Jts2Gsp_qMM%3A"
url = url.strip('\'"')
print url
header = {'User-Agent': 'Mozilla/5.0'} 
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')
anchors = soup.findAll('div')
links = [a['rg_meta'] for a in anchors if a.has_attr('rg_meta')]
images = []
def get_anchors(links):
	for a in anchors:
		links.append(a['jpg'])
	return links
	
raw_links = get_anchors(links)

for element in raw_links:
	if ".jpg" in str(element):
		#print element  
		raw_img = urllib2.urlopen("http:" + element).read()
		DIR="C:\\Users\\deez\\Desktop\\test\\"
		cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
		print cntr
		f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
		f.write(raw_img)
		f.close()