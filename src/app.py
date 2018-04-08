from sanic import Sanic
from sanic_graphql import GraphQLView
from lib.graphql.schema import schema
# import pdb; pdb.set_trace()

app = Sanic(__name__)
app.debug = True

app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=app.config.PORT)