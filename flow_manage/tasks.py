from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task


@shared_task
def flow_info():
    print("flow_info")
    time.sleep(10)
    return 100


# @shared_task
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
#     return


