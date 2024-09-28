from kafka import KafkaConsumer

# Crear el consumidor Kafka
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Leer desde el principio si no hay offset anterior
    group_id='my-group'
)

# Escuchar los mensajes
for message in consumer:
    print(f"Mensaje recibido: {message.value.decode('utf-8')}")