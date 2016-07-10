##@author klorox


from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import collections

print"""

                )           )           (      *                   (         (                      (     
     )   (   ( /(  (     ( /(           )\ ) (  `   (              )\ )  (   )\ )   (               )\ )  
  ( /(   )\  )\()) )\    )\())         (()/( )\))(  )\ )          (()/(  )\ (()/(   )\          (  (()/(  
  )\())(((_)((_)((((_)( ((_)\           /(_)((_)()\(()/(           /(_)(((_) /(_)((((_)(  `  )  )\  /(_)) 
 ((_)\ )\___ _((_)\ _ )\ _((_)         (_)) (_()((_)/(_))_        (_)) )\___(_))  )\ _ )\ /(/( ((_)(_))   
| | (_((/ __| || (_)_\(_| \| |         |_ _||  \/  (_)) __|       / __((/ __| _ \ (_)_\(_((_)_\| __| _ \  
|_  _| | (__| __ |/ _ \ | .` |          | | | |\/| | | (_ |       \__ \| (__|   /  / _ \ | '_ \| _||   /  
  |_|   \___|_||_/_/ \_\|_|\_|         |___||_|  |_|  \___|       |___/ \___|_|_\ /_/ \_\| .__/|___|_|_\  
                                                                                         |_|              
					written by klorox												 																						 																						 
																						 """

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'lxml')

def main(url):
	image_type = "image"
	print url
	header = {'User-Agent': 'Mozilla/5.0'} 
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, 'lxml')
	anchors = soup.findAll('a')
	links = [a['href'] for a in anchors if a.has_attr('href')]
		
	def get_anchors(links):
		for a in anchors:
			links.append(a['href'])
		return links
		
	raw_links = get_anchors(links)
	raw_links.sort()

	def get_duplicates(arr):
		dup_arr = arr[:]
		for i in set(arr):
			dup_arr.remove(i)       
		return list(set(dup_arr))   
		
	new_elements = get_duplicates(raw_links)

	def get_img():		
		for element in new_elements:
			if ".jpg" in str(element) or '.png' in str(element) or '.gif' in str(element):
				raw_img = urllib2.urlopen("http:" + element).read()
				DIR="C:\\Users\\deez\\Desktop\\test\\"
				cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
				print("Saving img: " + str(cntr) + "  :      " + str(element))
				f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
				f.write(raw_img)
				f.close()
	get_img()
	
board = raw_input("Enter the board letter (Example: b, x, wg, p): ")			
n = 2
firstTry = True
if firstTry == True:
	url = "http://boards.4chan.org/"+board+"/"
	main(url)
	firstTry = False
while n <= 10 and n >= 2 and firstTry == False:
	firstTry == False
	url = "http://boards.4chan.org/"+board+"/"+str(n)+"/"
	n = n + 1
	p = n - 1
	print("Page: " + str(p))
	main(url)
			
	
			
#main(url)		


