from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://jag:jag123@localhost/jag_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
