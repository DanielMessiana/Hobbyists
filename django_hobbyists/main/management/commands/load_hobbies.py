import json
from django.core.management.base import BaseCommand
from main.models import Hobby

class Command(BaseCommand):
    help = 'Load hobbies from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('hobby_data.json', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['hobby_data.json']
        with open(file_path) as f:
            data = json.load(f)
        for hobby_data in data:
            hobby = Hobby.objects.create(
                name=hobby_data['name'],
                sport=hobby_data['sport'].capitalize(),
                speed=hobby_data['speed'],
                intellectual=hobby_data['intellectual'],
                focus=hobby_data['focus'],
                social=hobby_data['social'],
                time=hobby_data['time'],
                creative=hobby_data['creative'],
                art=hobby_data['art'],
                craft=hobby_data.get('craft', ''),
                physicalexp=hobby_data['physicalexp'],
                cost=hobby_data['cost'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Hobby "{hobby}"'))
