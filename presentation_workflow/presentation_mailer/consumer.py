import json
import pika
from pika.exceptions import AMQPConnectionError
import django
import os
import sys
import time
from django.core.mail import send_mail


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presentation_mailer.settings")
django.setup()

while True:
    try:

        def process_approval(ch, method, properties, body):
            print("  Received %r" % body)
            content = json.loads(body)
            send_mail(
                "Your presentation has been accepted",
                f"{content['presenter_name']}, we're happy to tell you that your presentation {content['title']} has been accepted",
                "admin@conference.go",
                [f"{content['presenter_email']}"],
                fail_silently=False,
            )

        def process_rejection(ch, method, properties, body):
            print("  Received %r" % body)
            content = json.loads(body)
            send_mail(
                "Your presentation has been rejected",
                f"{content['presenter_name']}, we regret to inform you that your presentation {content['title']} has been rejected",
                "admin@conference.go",
                [f"{content['presenter_email']}"],
                fail_silently=False,
            )

        def main():
            parameters = pika.ConnectionParameters(host="rabbitmq")
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue="presentation_approvals")
            channel.basic_consume(
                queue="presentation_approvals",
                on_message_callback=process_approval,
                auto_ack=True,
            )
            channel.queue_declare(queue="presentation_rejections")
            channel.basic_consume(
                queue="presentation_rejections",
                on_message_callback=process_rejection,
                auto_ack=True,
            )
            channel.start_consuming()

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                print("Interrupted")
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

    except AMQPConnectionError:
        print("Could not connect to RabbitMQ")
        time.sleep(2.0)
