from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
	queryTerm = ""
	queryTerm = input("Enter the query term: ")
	html = urlopen("https://www.flipkart.com/search?q=" + queryTerm)
	soup = BeautifulSoup(html.read(), features="html.parser");
	list_product = soup.findAll('div', attrs={'class': '_3wU53n'})
	if list_product:
		for product in list_product:
			print(product.text)
	else:
		print("No results found!")

main() # call of the main function