import random
import custom as c
import time
import AccessTokenTest as a
import requests
from datetime import datetime
import time
import config as cfg
import json
import uuid


def request_handler(user_session, f):
    #txt_trans_req(user_session)
    return f(user_session)

def api_request_main(user_session, f):
    tt = random.choice(cfg.think_time)
    start_time = None
    start_time_pc = None
    end_time = None
    end_time_pc = None
    response_time = None
    test_name=None
    try:

        time.sleep(tt)
        start_time = datetime.now()
        start_time_pc = time.perf_counter()

        resp, test_name=request_handler(user_session, f)

        end_time = datetime.now()
        end_time_pc = time.perf_counter()
        response_time = (end_time_pc - start_time_pc) * 1000

        if resp is not None:
            try:
                resp_content = resp.json()
            except ValueError:
                resp_content = resp.text

            status_code = resp.status_code
            error_flag = 0 if resp.status_code in cfg.valid_status_codes + cfg.ignore_status_codes else 1


            status_code = resp.status_code
            error_flag = ""
            if resp.status_code in cfg.valid_status_codes:
                error_flag="P"
            elif resp.status_code in cfg.ignore_status_codes:
                error_flag="W"
            else:
                error_flag="F"

            return resp_content, status_code, error_flag, tt, test_name, start_time, start_time_pc, end_time, end_time_pc, response_time
        else:
            return "None", "0", "W", tt, test_name, start_time, start_time_pc, end_time, end_time_pc, response_time

    except Exception as e:
        print(e)
        return str(e), 0, 1, tt, test_name, start_time, start_time_pc, end_time, end_time_pc, response_time