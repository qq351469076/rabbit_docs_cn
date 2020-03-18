import time

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    # 默认auto_ack=True, 关闭以后, 需要下面的东西来进行确认
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 与rabbitmq建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('120.77.183.17'))
channel = connection.channel()

# 队列持久化
channel.queue_declare(queue='task_queue', durable=True)

# 在处理并确认上一条消息之前，不要将新消息发送给worker, 避免某个worker太过沉重
# 而是将其分派给不忙的下一个工作程序。
channel.basic_qos(prefetch_count=1)

# 特定的回调函数应该从hello队列接收消息
channel.basic_consume(queue='hello',
                      # auto_ack=True,
                      on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
