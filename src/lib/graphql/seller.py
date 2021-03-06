import graphene
from sanic import Sanic
from lib.graphql.product import Product, get_product
from lib.model import ProductModel

def get_seller(hit):
  data = hit['_source']
  return Seller(id=data['id'], identifier=data['identifier'], shortName=data['short_name'], fullName=data['full_name'])

class Seller(graphene.ObjectType):
  id = graphene.String()
  identifier = graphene.String()
  shortName = graphene.String()
  fullName = graphene.String()
  Products = graphene.List(lambda: Product)

  def resolve_Products(self, info):
    return map(get_product, ProductModel.get_results({'seller_identifier': self.identifier}))