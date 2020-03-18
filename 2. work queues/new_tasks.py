# coding: utf-8
import sys
from time import time

import pika

# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 将消息传递到hello队列, 队列持久化
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2)  # 使message持久化
                      )
print(" [x] Sent %r" % message)
