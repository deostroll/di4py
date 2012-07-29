# import the di module
# where we have written
# code to import any module 
# of choice. Those modules are
# defined in a file called di.xml

from di import getContainer
from pprint import pprint as pp

def main():
	
	# import the northwind
	# module in a container obejct
	container = getContainer('northwind')
	
	# now we have all types loaded 
	# in the above variable
	
	db = container.Products()
	
	# getting all products
	products = db.getAll()
	
	print '# All products'
	pp(products)
	
	# getting product with id 3
	product = db.get(3)
	
	print '\n# Retrieved product with id 3'
	print product
	
	# adding a new one
	p = container.Product()
	p.id = 4
	p.name = "Gizmo 4"
	p.price = '14.95'
	db.add(p)
	
	print '\n# Product after adding new item'
	pp(products) #reused reference
	
if __name__ == '__main__':
	main()

