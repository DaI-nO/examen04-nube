from kafka import KafkaProducer
import time

# Crear el productor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Enviar mensaje "Hola Mundo"
producer.send('test-topic', b'Hola Mundo')

# Forzar el envío de los mensajes
producer.flush()

print("Mensaje 'Hola Mundo' enviado.")
