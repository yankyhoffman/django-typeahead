from django.core.management.base import BaseCommand

from core.models import Person

SAMPLE_DATA = [
    ('Zaylee', 'Williamson'),
    ('Emerson', 'Beltran'),
    ('Kaydence', 'Hutchinson'),
    ('Korbin', 'O’Neal'),
    ('Treasure', 'Dyer'),
    ('Atreus', 'Webb'),
    ('Ariella', 'Norman'),
    ('Aziel', 'Carey'),
    ('Alora', 'Benton'),
    ('Jamal', 'Frye'),
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Person.objects.all().delete()

        for (first_name, last_name) in SAMPLE_DATA:
            Person.objects.create(first_name=first_name, last_name=last_name)
