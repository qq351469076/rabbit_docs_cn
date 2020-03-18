import sys

import pika

# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 交换机声明
channel.exchange_declare(exchange='logs',  # 交换机名称
                         exchange_type='fanout')  # 交换机类型 fanout, 将接收到的所有消息广播到它知道的所有队列中

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)

connection.close()
