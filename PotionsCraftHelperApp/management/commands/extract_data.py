from django.core.management.base import BaseCommand

from PotionsCraftHelperApp.models import Potion
import json
class Command(BaseCommand):

    def handle(self, *args, **options):
        potions = Potion.objects.all()
        data = []
        for potion in potions:
            data.append({
                'name': potion.name,
                'ingredients': potion.ingredients,
                'time': potion.time,
                'time_plus': potion.time_plus,
                'time_up_level': potion.time_up_level,
                'up_level': potion.up_level,
                'up_time': potion.up_time,
                'image': str(potion.image)
            })
        with open('potions_data.json', 'w') as file:
            json.dump(data, file, indent=4)