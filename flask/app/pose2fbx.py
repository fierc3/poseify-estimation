import pika

def notifyPose2Fbx(id: str, type: str):
    print("!!!!!!!!!!! Publishing Pose")
    rabbitmq_host = 'rabbitmq'
    queue_name = 'pose2fbx'

    credentials = pika.PlainCredentials('user', 'password')  # Use your RabbitMQ username and password
    connection_parameters = pika.ConnectionParameters(
        host=rabbitmq_host,
        credentials=credentials
    )
    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)

    # Publish a message
    message = "Ready to publish pose"
    message_properties = pika.BasicProperties(
    headers={
        'GUID': id,
        'Type': type
        },
    delivery_mode=2,  # Makes the message persistent
    )
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=message_properties
    )

    print(f"published pose {message}")

    connection.close()
