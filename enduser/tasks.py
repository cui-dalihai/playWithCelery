from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from enduser.models import EndUser


@shared_task
def time_wasted():
    print("time_wasted: sleep 10 seconds")
    time.sleep(10)

    EndUser(
        name='cui',
        age=18
    ).save()

    return 100


# @shared_task
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
#     return


