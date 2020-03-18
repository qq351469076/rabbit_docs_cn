import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()
channel.queue_declare(queue='hello')
# 特定的回调函数应该从hello队列接收消息
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
