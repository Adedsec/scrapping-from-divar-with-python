import json
import logging
from pprint import pprint
from time import sleep
import requests
from elasticsearch import Elasticsearch

# check and connect to elasticsearch


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connected')
    else:
        print('Awww it could not connect!')
    return _es

# creates index in elasticsearch server


def create_index(es_object, index_name):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "agahi": {
                "dynamic": "strict",
                "properties": {

                }
            }
        }
    }

    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(
                index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created

# stores records in elasticsearch (first checks that data not exists)


def store_record(elastic_object, index_name, record, data):
    is_stored = True
    jsonstring = elastic_object.count(index=index_name, body={
        "query": {"match": {"title": data['title']}}})

    count = jsonstring['count']
    if count > 0:
        print(' >><< Data Exists!')
        return False
    try:
        outcome = elastic_object.index(
            index=index_name, doc_type='numbers', body=record)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored
