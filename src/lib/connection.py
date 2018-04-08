from elasticsearch import Elasticsearch

def es(env):
  return Elasticsearch('{0}:{1}'.format(env.ELASTICSEARCH_HOST, env.ELASTICSEARCH_PORT))