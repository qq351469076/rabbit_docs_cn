import sys

import pika

# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

channel.basic_publish(
    exchange='topic_logs',
    # 发送到topic交换机的消息不能具有任意的routing_key-它必须是单词列表，以点分隔
    # 路由密钥中可以包含任意多个单词，最多255个字节。
    routing_key='anonymous.info',
    body='Hello World!')

print(" [x] Sent %r:%r" % ('anonymous.info', 'Hello World!'))

connection.close()
