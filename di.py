import xml.dom.minidom
import os
import importlib

__ctxt = None

def getObject(name):
	"""
	Reads the xml config
	and finds the corresponding 
	object node and initializes
	the required instance
	"""
	cdir = os.getcwd()
	global __ctxt
	if __ctxt is None:
		__ctxt = xml.dom.minidom.parse(os.path.join(cdir, 'di.xml'))
	objElements = __ctxt.getElementsByTagName('object')
	requiredObjectElement = filter(lambda x: x.attributes['name'].value == name, 
								objElements)
	typevals = requiredObjectElement[0].attributes['type'].value if len(requiredObjectElement) !=0 else None
	
	if typevals is None: 
		return typevals
	
	ditype, mod = map(str.strip, map(str, typevals.split(',')))
	k = importlib.import_module(mod)
	#TODO:
	# 1. Need way to safely import the Product type into __main__
	d = vars(k)
	x = d[ditype]
	return x()

