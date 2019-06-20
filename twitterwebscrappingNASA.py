import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "https://twitter.com/NASA"
thepage = urllib.request.urlopen (theurl)
soup = BeautifulSoup(thepage,"html.parser")

print (soup.title.text)

'''
for link in soup.findAll('a'):
    print (link.get('href'))
    print(link.text)
'''
print(soup.find('div', {"class":"ProfileHeaderCard"}) .find ('p').text)
i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print (i)
    print(tweets.find('p').text)
    i = i+1
    input("Press enter to exit ;)")


