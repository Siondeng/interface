import unittest
import requests

class LoginTest(unittest.TestCase):
    '''登录'''
    def setUp(self):
        self.base_url = "http://qa.eipsev.com/Login/UserLogin"

    def tearDown(self):
        print(self.result)

    def test_login_all_true(self):
        '''所有参数正确'''
        payload = {'Account':'deng.youjie','ChannlID':'4755505981213920512','DeviceType':'4','Password':'123'}
        r = requests.post(self.base_url,data = payload)
        self.result = r.json()
        self.assertEqual(self.result['Success'],True)

    def test_login_no_password(self):
        '''登录密码为空'''
        payload = {'Account': 'deng.youjie', 'ChannlID': '4755505981213920512', 'DeviceType': '4', 'Password': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['Success'], False)
        self.assertEqual(self.result['Message'],'登录密码不能为空!')

    def test_login_wrong_Account(self):
        '''不存在的用户名'''
        payload = {'Account': 'li.lianjie', 'ChannlID': '4755505981213920512', 'DeviceType': '4', 'Password': '123'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['Success'], False)
        self.assertEqual(self.result['Message'], '登录失败，用户名或者密码错误!')

if __name__ == '__main__':
    unittest.main()
