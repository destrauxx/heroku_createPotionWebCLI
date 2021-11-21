from django.core.management.base import BaseCommand

from PotionsCraftHelperApp.models import Potion
import json
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('potions_data.json', 'r') as file:
            data = json.load(file)
            for potion in data:
                created_data_potion = Potion()
                created_data_potion.name = potion['name']
                created_data_potion.ingredients = potion['ingredients']
                created_data_potion.time = potion['time']
                created_data_potion.time_plus = potion['time_plus']
                created_data_potion.time_up_plus = potion['time_up_level']
                created_data_potion.up_level = potion['up_level']
                created_data_potion.up_time = potion['up_time']
                created_data_potion.image = potion['image']
                created_data_potion.save()