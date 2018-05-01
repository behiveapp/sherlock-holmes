import graphene
from sanic import Sanic
from lib.model import SellerModel, ProductModel
from lib.graphql.seller import Seller, get_seller
from lib.graphql.product import Product, get_product

def get_query(**kwargs):
  map_fields = {"sellerIdentifier" : "seller_identifier", "category" : "categories"}
  for name, value in kwargs.items():
    if value:
      field_name = map_fields[name] if name in map_fields else name
      query = {field_name: value}
  return query

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String(), category=graphene.String(), sellerIdentifier = graphene.String())

  def resolve_Sellers(self, info, name):
    return list(map(get_seller, SellerModel.get_results({'short_name': name})))
  
  def resolve_Products(self, info, name = None, category = None, sellerIdentifier = None):
    query = get_query(name=name, category=category, sellerIdentifier=sellerIdentifier)
    return map(get_product, ProductModel.get_results(query))

schema = graphene.Schema(query=Query)
