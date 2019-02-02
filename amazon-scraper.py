from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
	queryTerm = ""
	queryTerm = input("Enter the query term: ")
	html = urlopen("https://www.amazon.in/s/field-keywords=" + queryTerm)
	soup = BeautifulSoup(html.read(), features="html.parser")
	list_product = soup.findAll('li', attrs={'class': 's-result-item celwidget'})[1:]
	if list_product:
		for product in list_product:
			print(product)
	else:
		print("No results found!")

main() # call of the main function