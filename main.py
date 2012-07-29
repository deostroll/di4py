# import the di module
# where we have written
# code to import any module 
# of choice. Those modules are
# defined in a file called di.xml

import di
from pprint import pprint as pp

productsDb = di.getObject('products')

print 'Getting all products'
pp(productsDb.getProducts())

print 'getting one product'
pp(productsDb.getProductById(2))


