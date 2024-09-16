from kafka import KafkaConsumer
consumer = KafkaConsumer('bankbranch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')
for msg in consumer:
    print(msg.value.decode("utf-8"))