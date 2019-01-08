from urllib.request import urlopen
from bs4 import BeautifulSoup

queryTerm = ""
queryTerm = input("Enter the query term: ")
html = urlopen("https://www.flipkart.com/search?q=" + queryTerm)
bsObj = BeautifulSoup(html.read());
print(bsObj.title)