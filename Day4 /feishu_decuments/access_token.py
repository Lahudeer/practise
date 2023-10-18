'''
Author: hongbinyang
LastEditTime: 2023-08-25 15:52:25
FilePath: /practise/Day4 /feishu_decuments/access_token.py
'''
import requests


class get_token:
    def __init__(self):
        self.app_id = "cli_a1eabb2f7d389013"
        self.app_secret = "oSBn6tX3Sf3dGz10H86r1cEqMntJYA8K"

    def get_app_access_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal'
        headers = {'Content-Type': "application/json; charset=utf-8"}
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        response = requests.post(url=url, headers=headers, json=data)
        try:
            app_access_token = response.json()['app_access_token']
            # print('app_access_token是{}'.format(app_access_token))
            return app_access_token
        except:
            print('获取app_access_token失败')

    def get_tenant_access_token(self):
        """
        获取当前用户的tenant_access_token
        """
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        headers = {'Content-Type': "application/json; charset=utf-8"}
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        response = requests.post(url=url, headers=headers, json=data)
        try:
            tenant_access_token = response.json()['tenant_access_token']
            # print('tenant_access_token是{}'.format(tenant_access_token))
            return tenant_access_token
        except:
            print('获取tenant_access_token失败')

    def get_refresh_token(self):
        """
        刷新获取当前用户的user_access_token
        """
        url = 'https://open.feishu.cn/open-apis/authen/v1/refresh_access_token'
        headers = {
            'Authorization': 'Bearer {}'.format(get_token().get_app_access_token()),
            'Content-Type': "application/json; charset=utf-8"
        }
        data = {
            'refresh_token': 'ur-cFAYtbJv54e9J.VsA_gVpyhl1dpw4lz1jo0041080E13',
            'grant_type': 'refresh_token'
        }
        response = requests.post(url=url, headers=headers, json=data)
        try:
            user_access_token = response.json()['data']['access_token']
            # print('user_access_token是{}'.format(user_access_token))
            return user_access_token
        except:
            print('获取user_access_token失败')


if __name__ == '__main__':
    # get_token().get_app_access_token()
    get_token().get_refresh_token()