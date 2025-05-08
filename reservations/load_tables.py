from django.core.management.base import BaseCommand
from reservations.models import Table
import os

class Command(BaseCommand):
    help = 'Load tables from text file'

    def handle(self, *args, **options):
        # Clear existing tables
        Table.objects.all().delete()
        
        # Read and execute each line
        with open('tables_data.txt', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    try:
                        exec(line.strip())
                        self.stdout.write(f"Created: {line.strip()}")
                    except Exception as e:
                        self.stderr.write(f"Error with {line.strip()}: {str(e)}")
        
        self.stdout.write("Finished loading tables!")