import graphene
from sanic import Sanic
from lib.model import SellerModel, ProductModel
from lib.graphql.seller import Seller, get_seller
from lib.graphql.product import Product, get_product

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String())

  def resolve_Sellers(self, info, name):
    return list(map(get_seller, SellerModel.get_results({'short_name': name})))
  
  def resolve_Products(self, info, name):
    return map(get_product, ProductModel.get_results({'name': name}))

schema = graphene.Schema(query=Query)
