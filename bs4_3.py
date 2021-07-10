#youtube tutorial
#STEP 0: setting up the environment
import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com/"

#STEP 1: GET THE HTML
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

#STEP 2:PARSE THE HTML
soup=BeautifulSoup(htmlContent,'html.parser')   #souping
#print(soup.prettify)       # prettify makes the soup more preety and easy to read


#STEP 3: HTML TREE TRAVERSAL

#commonly used types of object in bs4
# 1) Tag   print(type(title))
# 2)NavigableString    print(type(title.string))
# 3) Beautifulsoup    print(type(soup))
# 4) comment
# Get the title of the html page
title=soup.title
# Get all the paragraphs
#paras=soup.find_all('p')
#print(paras)
#Get first element in the html page
#print(soup.find('p')) # first paragraph
#print(soup.find('a')) # first anchor tag
# Get classess of any element in the html page
#print(soup.find('p')['class'])    #here it is ['lead', 'text-muted']
# suppose we want to find paragraph with a particular class
#print(soup.find_all('p',class_='lead'))
#print(soup.find_all('p',class_='text-muted'))
# Get the text from the tags / soup
#print(soup.find('p').get_text())
#print(soup.get_text()) # gives all the text without any tags and marks

#get all the anchors tag
anchors=soup.find_all('a')
##### VVVVVVV IMPORTANT #########Get all the links of the web page#######
#print(anchors)
all_links=set() # we form a blank link set.. set we used beacuase it will delever us one link no matter ho many times we repeated the link.. but it will give us only one

for link in anchors:
    if (link.get('href')!='#'):
        linktext="https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linktext)
