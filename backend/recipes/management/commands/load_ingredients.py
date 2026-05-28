import json
import os

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов из JSON-файла'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            default='/app/data/ingredients.json',
            help='Путь до JSON-файла с ингредиентами'
        )

    def handle(self, *args, **options):
        path = options['path']
        if not os.path.exists(path):
            self.stderr.write(f'Файл не найден: {path}')
            return
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        objs = [
            Ingredient(name=d['name'], measurement_unit=d['measurement_unit'])
            for d in data
        ]
        Ingredient.objects.bulk_create(objs, ignore_conflicts=True)
        self.stdout.write(
            self.style.SUCCESS(
                f'Успешно загружено: {Ingredient.objects.count()} ингредиентов'
            )
        )
