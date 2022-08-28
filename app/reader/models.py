from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reader(models.Model):
    ENGLISH = 'EN'
    SPANISH = 'SP'
    FRENCH = 'FR'

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    language = models.TextField(
        choices=(
            (ENGLISH, 'ENGLISH'),
            (SPANISH, 'SPANISH'),
            (FRENCH, 'FRENCH'),
        ),
        null=True
    )
    company = models.ForeignKey("Company", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Reader with title: {self.title} and langueage {self.get_language_display()}"


