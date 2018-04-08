import pdb
from sanic_graphql import GraphQLView
from sanic import Sanic
from sanic.response import json
from elasticsearch import Elasticsearch
# from schema import schema

app = Sanic(__name__)
app.debug = True

es = Elasticsearch('{0}:{1}'.format(app.config.ELASTICSEARCH_HOST, app.config.ELASTICSEARCH_PORT))

# app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

@app.route('/')
async def test(request):
  sellers_query = {'query': {'match': {'short_name': request.args['name'][0]}}}
  sellers_response = es.search(index='sellers', doc_type='sellers', body=sellers_query)['hits']['hits']

  products_query = {'query': {'match': {'name': request.args['name'][0]}}}
  products_response = es.search(index='products', doc_type='products', body=products_query)['hits']['hits']

  return json({'sellers': sellers_response, 'products': products_response})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=app.config.PORT)