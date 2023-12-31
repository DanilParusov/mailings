import schedule
import time

from django.core.management import BaseCommand

from sender.services import check_mail_sender


class Command(BaseCommand):

    def handle(self, *args, **options):
        """команда для запуска проверки активных рассылок"""
        schedule.every(3).seconds.do(check_mail_sender)

        while True:
            schedule.run_pending()
            time.sleep(1)