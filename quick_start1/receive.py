import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

channel = connection.channel() #подключаемся к брокеру сообщений
channel.queue_declare(queue='hello')
print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    #При получении каждого сообщения библиотека Pika вызывает эту callback функцию.
    print ("[x] Received %r" % (body,))

channel.basic_consume(callback, queue='hello', no_ack=True) #callback функция будет получать сообщения из очереди с именем «hello»:
channel.start_consuming()