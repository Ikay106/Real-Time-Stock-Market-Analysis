from kafka import KafkaConsumer
import json
import time

# --- Configuration matching the Producer ---
consumer = KafkaConsumer(
    'stock_analysis',                           # Topic name (must match what producer sends to)
    bootstrap_servers=['localhost:9094'],       # External listener from your compose.yml
    auto_offset_reset='earliest',               # Start reading from the beginning if no offset
    enable_auto_commit=True,                    # Automatically commit offsets
    group_id='my-consumer-group',               # Consumer group name (allows multiple consumers)
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON bytes → dict
)

print("Starting Kafka consumer. Waiting for messages on topic 'stock_analysis'...")

for message in consumer:
    data = message.value
    # Print the received data
    print(f"Value (Deserialized): {data}")
    
    # Optional: add a small delay so console doesn't flood too fast
    time.sleep(1)

# Cleanup (this line usually runs when you Ctrl+C to stop)
consumer.close()
print("Kafka consumer closed.")