import graphene
from sanic import Sanic

def get_product(hit):
  data = hit['_source']
  return Product(id=data['id'], sellerIdentifier=data['seller_identifier'], code=data['code'], name=data['name'], categories=data['categories'],  price=data['price'],  description=data['description'])

class Product(graphene.ObjectType):
  id = graphene.String()
  sellerIdentifier = graphene.String()
  name = graphene.String()
  code = graphene.String()
  categories = graphene.List(graphene.String)
  price = graphene.Float()
  description = graphene.String()