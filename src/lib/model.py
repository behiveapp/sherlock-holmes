from lib.connection import es

class SellerModel:
  @classmethod
  def get_results(self, query):
    body = {'query': {'match': query}}
    return es.search(index='sellers', doc_type='sellers', body=body)['hits']['hits']
    
class ProductModel:
  @classmethod
  def get_results(self, query):
    body = {'query': {'match': query}}
    return es.search(index='products', doc_type='products', body=body)['hits']['hits']
    