import requests
from access_token import get_token
token = get_token().get_refresh_token()


class FeiShuDocument:
    def __init__(self):
        self.base_url = "https://open.feishu.cn/open-apis"
        self.headers = {'Authorization': 'Bearer {}'.format(token)}

    def create_document(self, folder_token, title):
        """
        创建 飞书 文档
        :param folder_token: 文件夹token，复制文件夹链接飞书打开可获取
        :param title: 文档标题
        :return document_id: 文档唯一标识id
        """
        url = self.base_url+'/docx/v1/documents'
        data = {
                "folder_token": folder_token,
                "title": title
        }
        response = requests.post(url=url, headers=self.headers, json=data)
        if response.status_code == 200:
            print('创建文档 {} 成功'.format(title))
            document_id = response.json()['data']['document']['document_id']
            return document_id
        else:
            print('创建文档 {} 失败,失败原因{}'.format(title, response.json()))
            return '创建文档 {} 失败,失败原因{}'.format(title, response.json())

    def get_all_blocks(self, document_id):
        """获取文档所有块"""
        url = self.base_url + "/docx/v1/documents/{}/blocks".format(document_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def get_raw_content(self, document_id):
        """获取文档纯文本内容"""
        url = self.base_url + '/docx/v1/documents/{}/raw_content'.format(document_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def get_doc_info(self, document_id):
        """获取文档基本信息"""
        url = self.base_url + '/docx/v1/documents/{}'.format(document_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def get_blocks(self, document_id, block_id):
        """获取具体块信息"""
        url = self.base_url + '/docx/v1/documents/{}/blocks/{}'.format(document_id, block_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def add_blocks(self, document_id, block_id, data):
        """
        创建飞书文档 块
        :param document_id: 文档唯一标识id
        :param block_id: 块唯一标识id
        :param data: 接口请求体
        :return:
        """
        url = self.base_url+'/docx/v1/documents/{}/blocks/{}/children'.format(document_id, block_id)
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("创建文档块:{}".format(response.json()))

    def update(self, document_id, block_id, data):
        """更新块"""
        url = self.base_url + '/docx/v1/documents/{}/blocks/{}'.format(document_id, block_id)
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def batch_update(self, document_id, data):
        """批量更新块"""
        url = self.base_url + '/docx/v1/documents/{}/blocks/batch_update'.format(document_id)
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def batch_delete(self, document_id, block_id, data):
        """批量删除块,需要块下面含有子块"""
        url = self.base_url + '/docx/v1/documents/{}/blocks/{}/children/batch_delete'.format(document_id, block_id)
        response = requests.delete(url, headers=self.headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))

    def children(self, document_id, block_id):
        """获取所有子块"""
        url = self.base_url + '/docx/v1/documents/{}/blocks/{}/children'.format(document_id, block_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("接口请求失败:{}".format(response.json()))


if __name__ == '__main__':
    FeiShuDocument().create_document("IBgUfcbKWlpj8DdmrWycIrNnnpd", "测试周报文档")