import graphene
from sanic import Sanic

def get_product(hit):
  data = hit['_source']
  return Product(sellerIdentifier=data['seller_identifier'], code=data['code'], name=data['name'])

class Product(graphene.ObjectType):
  sellerIdentifier = graphene.String()
  name = graphene.String()
  code = graphene.String()