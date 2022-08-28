from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from reader.models import Reader
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Processes reader files'

    def add_arguments(self, parser):
        parser.add_argument('file-name', nargs='+', type=str)

    def handle(self, *args, **options):
        app_root_path = Path(__file__).resolve().parent.parent.parent.parent
        files_path = os.path.join(app_root_path, "files")
        file_name = options['file-name'][0]

        with open(files_path + '/' + file_name) as f:
            lines = f.read()
            r = Reader(title=file_name, content=lines)
            r.save()

        self.stdout.write(self.style.SUCCESS("Reading file with title"))


