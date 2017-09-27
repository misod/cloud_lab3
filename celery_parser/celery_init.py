from __future__ import absolute_import
from celery_init import Celery

app = Celery('celery_parser',
             broker='amqp://jag:jag123@localhost/jag_vhost',
             backend='rpc://',
             include=['celery_parser.parsning'])
