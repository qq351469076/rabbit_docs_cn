import sys

import pika

# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 定义交换机direct_logs和类型
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 订阅交换机direct_logs, 绑定info队列
channel.basic_publish(exchange='direct_logs', routing_key='info', body=message)

print(" [x] Sent %r:%r" % ('info', message))

connection.close()
