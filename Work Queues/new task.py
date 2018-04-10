#!/usr/bin/env python
import pika
import sys

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.208.14.4'))

credentials = pika.PlainCredentials('prashant', 'prashant')
parameters = pika.ConnectionParameters('10.208.14.4', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()