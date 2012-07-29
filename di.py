import xml.dom.minidom
import os
import importlib
from pprint import pprint as pp
__ctxt = None

class context: pass

def getContainer(name=''):
	"""
	Reads the xml config
	and finds the corresponding 
	object node and initializes
	the required instance
	"""
	if name == '':
		return None
	
	cdir = os.getcwd()
	global __ctxt
	if __ctxt is None:
		__ctxt = xml.dom.minidom.parse(os.path.join(cdir, 'di.xml'))
	objElements = __ctxt.getElementsByTagName('module')
	filtered = filter(lambda x: x.attributes['name'].value == name, 
								objElements)
	if len(filtered) == 0:
		return None
	
	mElement = filtered[0]
	
	module = importlib.import_module(str(mElement.attributes['name'].value))
	
	ctxt = context()
	
	for n, v in vars(module).items():
		if n[0] == '_':
			continue
		setattr(ctxt, n, v)
	
	return ctxt
	

