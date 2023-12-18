from django.core.management.base import BaseCommand, CommandError
from duuni_app.models import JobListing, ProgrammingLanguage
from django.core.management import call_command
from django.db import connections
class Command(BaseCommand):
    help = 'My custom startup command'

    def handle(self, *args, **kwargs):
        # Assuming 'default' is the name of your database connection in settings.py
        database_name = 'default'

        # Run the flush management command to reset the database
        call_command('flush', interactive=False, database=database_name)

        # Close the database connection to avoid any issues
        connections[database_name].close()

