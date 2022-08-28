from django.contrib.auth import get_user_model
from django.test import TestCase
from core import models
from decimal import Decimal
# Create your tests here.


class ModelTests(TestCase):

    def test_create_recipe(self):
        recipe = models.Recipe.objects.create(
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description.',
            link='http://example.pdf'
        )

        self.assertEqual(str(recipe), recipe.title)

