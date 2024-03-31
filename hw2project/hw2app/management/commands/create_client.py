from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John',
                        email='john@example.com',
                        phone_number='12345',
                        address='street')
        client.save()
        self.stdout.write(f'{client} created')
