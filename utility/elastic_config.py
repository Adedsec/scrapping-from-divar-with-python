import json
import logging
from pprint import pprint
from time import sleep

import requests
from elasticsearch import Elasticsearch


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connected')
    else:
        print('Awww it could not connect!')
    return _es


def create_index(es_object, index_name):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "numbers": {
                "dynamic": "strict",
                "properties": {
                    "number": {
                        "type": "number"
                    },
                    "category": {
                        "type": "text"
                    },
                    "main-category": {
                        "type": "text"
                    },
                    "title": {
                        "type": "text"
                    }
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


def store_record(elastic_object, index_name, record, my_id):
    is_stored = True
    try:
        outcome = elastic_object.index(
            index=index_name, doc_type='numbers', body=record, id=my_id)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored
