from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
