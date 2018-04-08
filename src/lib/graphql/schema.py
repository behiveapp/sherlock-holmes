import graphene
from sanic import Sanic
from lib.model import SellerModel, ProductModel
from lib.graphql.seller import Seller, get_seller
from lib.graphql.product import Product, get_product

env = Sanic(__name__).config

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String())

  def resolve_Sellers(self, info, name):
    seller = SellerModel(env)
    return list(map(get_seller, seller.get_results({'short_name': name})))
  
  def resolve_Products(self, info, name):
    product = ProductModel(env)
    return map(get_product, product.get_results({'name': name}))

schema = graphene.Schema(query=Query)
