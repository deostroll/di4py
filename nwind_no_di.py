# northwind sample
# without di

import northwind as nw
from pprint import pprint as pp

def main():
	
	db = nw.Products()
	
	# getting all products
	products = db.getAll()
	
	print '\n# All products'
	pp(products)
	
	# getting product with id 3
	product = db.get(3)
	
	print '\n# product with id 3'
	pp(product)
	
	# adding new product
	p = nw.Product()
	p.id = 4
	p.name = 'Gizmo 4'
	p.price = '14.95'
	db.add(p)
	
	print '\n# Listing all products'
	pp(db.getAll())
	

if __name__ == '__main__':
	main()
	
	
