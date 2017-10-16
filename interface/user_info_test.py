import unittest
import requests
import get_cookie
class UserInfoTest(unittest.TestCase):
    '''用户信息'''
    def setUp(self):
        self.base_url1 = "http://qa.eipsev.com/user/GetCurrentUserInfo"#个人中心
        self.base_url2 = "http://qa.eipsev.com/UserMessage/GetUserMessage"#首页消息
        self.cookie = get_cookie.get_cookies()

    def tearDown(self):
        print (self.result)

    def test_get_userinfo(self):
        '''获取个人中心信息'''
        r = requests.get(self.base_url1,cookies = self.cookie)
        self.result = r.json()
        self.assertEqual(self.result["Success"],True)
        self.assertEqual(self.result['Data']['Company'], '跨境通')

    def test_get_usermessage(self):
        '''获取首页消息'''
        r = requests.get(self.base_url2, cookies=self.cookie)
        self.result = r.json()
        self.assertEqual(self.result["Success"], True)

    if __name__ == '__main__':
        unittest.main()

