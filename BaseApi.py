
import yaml
import logging
import requests

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

S = requests.Session()
class ApiHelper():
    def user_login(self):
        try:
            result = S.post(url=testdata['url'], data={'username': testdata['login'], 'password': testdata['password']})
            response_json = result.json()
            token = response_json.get('token')
        except:
            logging.exception(f"Exception get {token}")
            return None
        logging.info(f"Token get successful")
        return token

    def get_user(self):
        try:
            result_get_user = S.post(url=testdata['url'], headers={'X-Auth-Token': self.user_login()},
                                     data={'username': testdata['username'], 'password': testdata['password']})
            response_json = result_get_user.json()
            user_id = response_json.get('id')
        except:
            logging.exception(f"Exception create post {result_get_user}")
            return None
        logging.info(f"Get user info successful")
        return user_id

    def user_info(self):
        try:
            result_get_info = S.get(url=testdata['post_address'],
                                    headers={'X-Auth-Token': self.user_login()})
            response_json = result_get_info.json()
            userid = response_json.get('id')
        except:
            logging.exception(f"Exception create post {result_get_info}")
            return None

        logging.info(f"Get user info successful")
        return userid