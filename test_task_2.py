import logging
import yaml
from BaseApi import ApiHelper


with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)



def test_task_2():
    logging.info("test_rest_api Starting")
    checkers = ApiHelper()
    checkers.get_user()
    checkers.user_info()
    assert checkers.user_info() == checkers.get_user()

