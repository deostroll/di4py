class Product:
	def __init__(self, id, name, price):
		self.id = id
		self.name = name
		self.price = price
	def __str__(self):
		return str({
			'id': self.id,
			'name': self.name,
			'price': self.price
			})
	def __repr__(self):
		return self.__str__()
		
class Products:
	def __init__(self):
		p = Product(1, 'Gizmo 1', '12.25')
		p2 = Product(2, 'Gizmo 2', '1.45')
		p3 = Product(3, 'Gizmo 3', '10.25')
		self.__products = [p, p2, p3]
	
	def getProductById(self, id):
		item = filter(lambda p: p.id == id, self.__products)
		if len(item) == 0: 
			return None
		else:
			return item[0]
	
	def getProducts(self):
		return self.__products

	def addProduct(self, product):
		if isinstance(product, Product):
			self.__products.append(product)
		else:
			print 'not added'
		
		
