from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task


@shared_task
def issue_create():
    print("create issue")
    time.sleep(10)
    return 101


@shared_task
def priorities():
    print("priorities")
    time.sleep(10)
    return 102



