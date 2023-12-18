from django.core.management.base import BaseCommand, CommandError
from duuni_scraper.main import webscrape
from duuni_app.models import JobListing, ProgrammingLanguage
from django.core.management import call_command
from django.db import connections
class Command(BaseCommand):
    help = 'My custom startup command'

    def handle(self, *args, **kwargs):
        def is_database_empty():
            return not JobListing.objects.exists()


        if is_database_empty():
            print("Database is empty")
            webscrape()
            C_language = ProgrammingLanguage.objects.filter(name='C ')
            for lan in C_language:
                lan.name = "C"
                lan.save()


            
        for entry in JobListing.objects.all():
            print(f"Entry: {entry.title}")
            print("Languages:")
            for language in entry.programming_languages.all():
                print(f"- {language.name}")


            

        print("Initialization completed")
