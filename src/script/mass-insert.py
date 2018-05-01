import os
import random
from elasticsearch import Elasticsearch

es = Elasticsearch('{0}:{1}'.format(os.environ['SANIC_ELASTICSEARCH_HOST'], os.environ['SANIC_ELASTICSEARCH_PORT']))
es.indices.delete(index='sellers')
es.indices.delete(index='products')

identifiers = ['01001001000113', '02002002000226', '03003003000339', '67147304624', '35455326236', '87825205693', '19163724901', '43026382221', '65641660604', '78920737525', '31444420623', '42443738370', '31760664499', '37699776291', '63362321909', '24680731699', '28192281949', '31327639696', '11073242897']
first_name_parts = ['Casas', 'Grupos', 'Empreiteiras', 'Imobiliárias', 'Armazéns', 'Papelarias', 'Docerias']
second_name_parts = ['Ruth', 'Bahia', 'Baiao', 'Famous', 'Joe', 'Brothers', 'Manhield']
third_name_parts = ['SA', 'LTDA', 'Eirelli', 'MEI']

product_codes = ['code01', 'code02', 'code03', 'code04', 'code05']
product_names = ['Produto legal', 'Produto bacana', 'Produto show', 'Produto bonito', 'Produto grande', 'Produto pequeno', 'Produto feio', 'Produto caro', 'Produto barato', 'Produto chato', 'Produto inovador', 'Produto novo', 'Produto antigo', 'Produto velho', 'Produto Bahia', 'Produto Joe']
product_categories = ['Culinária', 'Culinária Francesa', 'Culinária Italiana', 'Roupas e Acessórios', 'Ferramentas', 'Instrumentos Musicais']

for identifier in identifiers:
  short_name = "{0} {1}".format(random.choice(first_name_parts), random.choice(second_name_parts))
  full_name = "{0} {1}".format(short_name, random.choice(third_name_parts))
  es.index(index='sellers', doc_type='sellers', body= {
      "id": random.randrange(1000000000),
      "identifier": identifier,
      "full_name": full_name,
      "short_name": short_name
  })

  for code in product_codes:
    es.index(index='products', doc_type='products', body= {
      "id": random.randrange(1000000000),
      "seller_identifier": identifier,
      "code": code,
      "name": random.choice(product_names),
      "categories": [random.choice(product_categories), random.choice(product_categories)],
      "description" : "A brief description of the product",
      "price": round(random.uniform(7,50), 2)
    })



