import imp
#jsonrpc = imp.load_source('jsonrpc', '/Users/niki/ownCloud/Main/work/ESSENCE/research/integration/code/stanford-corenlp-python/jsonrpc.py')
jsonrpc = imp.load_source('jsonrpc', os.path.join(os.path.dirname(__file__), 'jsonrpc.py')

import json
#from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint


class StanfordNLP:
	def __init__(self):
		self.server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("127.0.0.1", 8080)))    
	def parse(self, text):
 		return json.loads(self.server.parse(text))


snlp = StanfordNLP()
result = snlp.parse("Hello world! It is so beautiful.")
pprint(result)

from nltk.tree import Tree
tree = Tree.fromstring(result['sentences'][0]['parsetree'])
pprint(tree)
