

from bs4 import BeautifulSoup
import requests
import re
import os
from urllib.request import urlopen
import collections
from PIL import Image    
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True                                                                            

print("""

                )           )           (      *                   (         (                      (     
     )   (   ( /(  (     ( /(           )\ ) (  `   (              )\ )  (   )\ )   (               )\ )  
  ( /(   )\  )\()) )\    )\())         (()/( )\))(  )\ )          (()/(  )\ (()/(   )\          (  (()/(  
  )\())(((_)((_)((((_)( ((_)\           /(_)((_)()\(()/(           /(_)(((_) /(_)((((_)(  `  )  )\  /(_)) 
 ((_)\ )\___ _((_)\ _ )\ _((_)         (_)) (_()((_)/(_))_        (_)) )\___(_))  )\ _ )\ /(/( ((_)(_))   
| | (_((/ __| || (_)_\(_| \| |         |_ _||  \/  (_)) __|       / __((/ __| _ \ (_)_\(_((_)_\| __| _ \  
|_  _| | (__| __ |/ _ \ | .` |          | | | |\/| | | (_ |       \__ \| (__|   /  / _ \ | '_ \| _||   /  
  |_|   \___|_||_/_/ \_\|_|\_|         |___||_|  |_|  \___|       |___/ \___|_|_\ /_/ \_\| .__/|___|_|_\  
                                                                                         |_|              
				      written by Devin Adams											 																						 																						 
																						 """

	)
	
	# Gather our HTML source code from the pages
	
def get_soup(url,header):
  return BeautifulSoup(urlopen(urllib2.request(url, headers=header)), 'lxml')

	# Main logic function, we use this to re-iterate through the pages
	
def main(url):
	image_name = "image"
	print(url)
	header = {'User-Agent': 'Mozilla/5.0'} 
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, 'lxml')
	anchors = soup.findAll('a')
	links = [a['href'] for a in anchors if a.has_attr('href')]
	
	# Grabs all the a anchors from the HTML source which contain our image links
	
	def get_anchors(links):
		for a in anchors:
			links.append(a['href'])
		return links

	# Gather the raw links and sort them
	
	raw_links = get_anchors(links)
	raw_links.sort()

	# Parse out any duplicate links
	def get_duplicates(arr):
		dup_arr = arr[:]
		for i in set(arr):
			dup_arr.remove(i)       
		return list(set(dup_arr))   
		
	# Define our list of new links and call the function to parse out duplicates
	
	new_elements = get_duplicates(raw_links)

	# Get the image links from the raw links, make a request, then write them to a folder.
	
	def get_img():		
		for element in new_elements:
			if ".jpg" in str(element) or '.png' in str(element) or '.gif' in str(element):
				retries = 0
				passed = False
				
	# Retry scraping 3 times on the element if exception is thrown
	
				while(retries < 3):	
					try:
	# Check if the link uses HTTPS or HTTP, not sure why but 4chan switches between the 2
	
						if "https:" not in element and "http:" not in element:
							element = "http:"+element	
	# Read the element
	
						raw_img = urlopen(element).read()
	# Check previous file names to determine our new one.
	
						cntr = len([i for i in os.listdir(dirr) if image_name in i]) + 1
						print("Saving img: " + str(cntr) + "  :      " + str(element) + " to: "+ dirr )
	# Write the file
						with open(dirr + image_name + "_"+ str(cntr)+".jpg", 'wb') as f:
							f.write(raw_img)
						passed = True
						break
					except urllib2.URLError as e:
						retries += 1
						print("Failed on", element, "(Retrying", retries, ")")
				if not passed:
					print("Failed on ", element, "skipping...")
				
# Call our image writing function

	get_img()

# Ask the user which board they would like to use and directory they would like to save in

print("""Boards: [a / b / c / d / e / f / g / gif / h / hr / k / m / o / p / r / s / t / u / v / vg / vr / w / wg] [i / ic] [r9k] [s4s] [cm / hm / lgbt / y] [3 / aco / adv / an / asp / biz / cgl / ck / co / diy / fa / fit / gd / hc / his / int / jp / lit / mlp / mu / n / news / out / po / pol / qst / sci / soc / sp / tg / toy / trv / tv / vp / wsg / wsr / x]""")	
print("\n")
board = input("Enter the board letter (Example: b, p, w): ")
dirr = input("Enter the working directory (USE DOUBLE SLASHES): ")

# Open the directory

os.startfile(dirr)

# Define our starting page number and first try value

page = 2
firstTry = True

# Check if this is the first iteration

if firstTry == True:
	url = "http://boards.4chan.org/"+board+"/"
	firstTry = False
	main(url)
	# After first iteration, this loop changes the url after each completed page by calling our main function again each time.
	while page <= 10 and page >= 2 and firstTry == False:
		firstTry == False
		url = "http://boards.4chan.org/"+board+"/"+ str(page) +"/"
		page = page + 1
		p = page - 1
		print("Page: " + str(p))
		main(url)
		
		
			
	
			

