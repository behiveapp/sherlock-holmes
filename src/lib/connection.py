import os
from elasticsearch import Elasticsearch

es = Elasticsearch('{0}:{1}'.format(os.environ['SANIC_ELASTICSEARCH_HOST'], os.environ['SANIC_ELASTICSEARCH_PORT']))