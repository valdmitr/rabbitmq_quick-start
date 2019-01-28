import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep( len(body) )
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) #подписчик не получит новое сообщение, до тех пор пока не обработает и не подтвердит предыдущее. RabbitMQ передаст сообщение первому освободившемуся подписчику.
channel.basic_consume(callback, queue='task_queue') #callback функция будет получать сообщения из очереди с именем «hello»:
channel.start_consuming()