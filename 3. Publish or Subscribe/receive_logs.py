import pika


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 交换机声明
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 让服务器为我们选择一个随机队列名称, 一旦消费者连接关闭，则应删除队列。
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 告诉交换机将消息发送到哪个队列
channel.queue_bind(exchange='logs', queue=result.method.queue)

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
