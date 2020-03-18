import sys

import pika


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 义交换机direct_logs和类型
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 定义随机队列, 用完即删
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = ['info']

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
