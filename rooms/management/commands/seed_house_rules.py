from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates amenities"

    def handle(self, *args, **options):
        amenities = [
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming Pool",
            "Toilet",
            "Towels",
            "TV",
        ]

        for a in amenities:
            room_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))