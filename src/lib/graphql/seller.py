import graphene
from sanic import Sanic
from lib.graphql.product import Product, get_product
from lib.model import ProductModel

def get_seller(hit):
  data = hit['_source']
  return Seller(identifier=data['identifier'], shortName=data['short_name'], fullName=data['full_name'])

env = Sanic(__name__).config

class Seller(graphene.ObjectType):
  identifier = graphene.String()
  shortName = graphene.String()
  fullName = graphene.String()
  Products = graphene.List(lambda: Product)

  def resolve_Products(self, info):
    product = ProductModel(env)
    return map(get_product, product.get_results({'seller_identifier': self.identifier}))