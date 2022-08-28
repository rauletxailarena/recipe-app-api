from decimal import Decimal
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipes:recipe-list')

def create_recipe(**params):
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdb'
    }
    defaults.update(params)
    recipe = Recipe.objects.create(**defaults)
    return recipe


class PublicRecipeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()


    def test_retrieve_recipes(self):
        create_recipe()
        create_recipe()

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_filter_by_minutes(self):
        r1 = create_recipe(time_minutes=2, title='Pasta')
        r2 = create_recipe(time_minutes=4, title='Fish')
        r3 = create_recipe(time_minutes=6, title='Meat')
        r4 = create_recipe(time_minutes=8, title='Veggies')

        params = {'time_minutes': 4}
        res = self.client.get(RECIPES_URL, params)

        s1 = RecipeSerializer(r1)
        s2 = RecipeSerializer(r2)
        s3 = RecipeSerializer(r3)
        s4 = RecipeSerializer(r4)

        self.assertIn(s1.data, res.data)
        self.assertIn(s2.data, res.data)
        self.assertNotIn(s3.data, res.data)
        self.assertNotIn(s4.data, res.data)
