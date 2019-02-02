from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint

def main():
	queryTerm = ""
	queryTerm = input("Enter the query term: ")
	html = urlopen("https://www.amazon.in/s/field-keywords=" + queryTerm)
	soup = BeautifulSoup(html.read(), features="html.parser")
	list_product = soup.findAll('div', attrs={'class': 'a-fixed-left-grid-col a-col-right'})
	products = []
	if list_product:
		for product in list_product:
			if product.find('a', attrs={'class': 'a-link-normal a-text-normal'}):
				name  = product.find('a', attrs={'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'}).text
				price = product.find('a', attrs={'class': 'a-link-normal a-text-normal'}).text
				product = {
					'name': name,
					'price': price
				}
				products += [product]

		print(products)

	else:
		print("No results found!")

main() # call of the main function