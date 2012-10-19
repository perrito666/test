# -*- coding: utf-8 *-*
from django.core.management.base import BaseCommand, CommandError
from devotional.models import Devotional
import csv


from pprint import pprint as pp
class Command(BaseCommand):
    args = "<csv_filepath>"
    help = "Imports a tab file"

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError("No file path provided")
        file_path = args[0]
        with open(file_path, "r") as csvfile:
            devreader = csv.DictReader(csvfile, skipinitialspace=True)
            for csv_args in devreader:
                Devotional.objects.create(**csv_args)

