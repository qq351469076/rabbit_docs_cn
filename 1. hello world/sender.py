# coding: utf-8
from time import time
import pika

# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()
# 将消息传递到hello队列
channel.queue_declare(queue='hello')
# 使用由空字符串标识的默认交换, 这种交换是特殊的‒它使我们可以准确地指定消息应进入的队列。
channel.basic_publish(exchange='',
                      # 队列名称需要在routing_key参数中指定
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
# 关闭连接
connection.close()
