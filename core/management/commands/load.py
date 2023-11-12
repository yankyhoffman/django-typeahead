import itertools

from django.core.management.base import BaseCommand

from core.models import Person

FIRST_NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack', 'Katie', 'Lily',
               'Mason', 'Nathan', 'Owen', 'Penny', 'Quinn', 'Riley', 'Sam', 'Tori', 'Ursula', 'Violet', 'Walter',
               'Xavier', 'Yvonne', 'Zachary']
LAST_NAMES = ['Adams', 'Brown', 'Clark', 'Davis', 'Evans', 'Flores', 'Garcia', 'Harris', 'Jackson', 'King', 'Lee',
              'Morgan', 'Nelson', 'Parker', 'Roberts', 'Scott', 'Smith', 'Taylor', 'Thompson', 'White', 'Wright']


class Command(BaseCommand):
    def handle(self, *args, **options):
        Person.objects.all().delete()

        for first, last in itertools.product(FIRST_NAMES, LAST_NAMES):
            Person.objects.create(first_name=first, last_name=last)
