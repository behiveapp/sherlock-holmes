from sanic_graphql import GraphQLView
from sanic import Sanic
from sanic.response import json
# from schema import schema

app = Sanic(__name__)
app.debug = True


# app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

@app.route('/')
async def test(request):
    return json({'hello': 'worlds'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config.PORT)