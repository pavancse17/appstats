import csv

from django.core.management import BaseCommand, CommandError

from adjust_app.models import AppStat


class Command(BaseCommand):
    help = "Imports data from csv file writes to AppStat Model"

    def handle(self, *args, **options):
        with open('adjust_app/data/dataset.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar="\"")
            field_names = next(reader)

            for row in reader:
                app_stat = AppStat()

                for i, field in enumerate(row):
                    if field_names[i] == "os":
                        if field.strip() == "android":
                            field = AppStat.ANDROID
                        elif field.strip() == "ios":
                            field = AppStat.IOS
                    setattr(app_stat, field_names[i], field)

                try:
                    app_stat.save()
                except Exception as e:
                    raise CommandError(e)
