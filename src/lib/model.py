from lib.connection import es

class Model:
  def __init__(self, env):
    self.env = env

class SellerModel(Model):
  def get_results(self, query):
    body = {'query': {'match': query}}
    return es(self.env).search(index='sellers', doc_type='sellers', body=body)['hits']['hits']
    
class ProductModel(Model):
  def get_results(self, query):
    body = {'query': {'match': query}}
    return es(self.env).search(index='products', doc_type='products', body=body)['hits']['hits']
    