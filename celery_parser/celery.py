from __future__ import absolute_import
from celery import Celery

app = Celery('celery_parser',
             broker='amqp://micke:micke123@localhost/micke_vhost',
             backend='rpc://',
             include=['celery_parser.parsning'])
