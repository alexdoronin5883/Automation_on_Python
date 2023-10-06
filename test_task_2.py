import logging
import yaml
from BaseApi import ApiHelper


with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)



def test_task_2():
    """
    get_user() получает "id"  с запросом post
    user_info получает "id" с запросом get
    assert срвнивает значения 
    """
    logging.info("test_rest_api Starting")
    checkers = ApiHelper()
    checkers.get_user()
    checkers.user_info()
    assert checkers.user_info() == checkers.get_user()

