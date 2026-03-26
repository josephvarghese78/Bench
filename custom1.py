import random
import time
import requests
from datetime import datetime
import time
import config as cfg
import json
import uuid
from decorators import task
from requests.models import Response

class api_requests:

    @task(name='ttddssrr', weight=2)
    def tdsr(self, user_session):
        resp= user_session.get("http://nl:3200/expense/tdsr", timeout=10000, verify=True)

        return resp,  self.tdsr.test_name