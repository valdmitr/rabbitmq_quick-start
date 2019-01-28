import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
)) #создаем соединение

channel = connection.channel() #подключаемся к брокеру сообщений
channel.queue_declare(queue='hello') #создаем очередь под названием "hello"
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent'Hello World!'")
connection.close()