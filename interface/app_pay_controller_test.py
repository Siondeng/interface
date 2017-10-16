import unittest
import requests
import time
import datetime
import get_cookie

class LeaveController(unittest.TestCase):
    '''报销'''
    def setUp(self):
        self.base_url = "http://qa.eipsev.com//ApplicationForPay/SubmitApplicationForPay"
        self.cookie = get_cookie.get_cookies()



    def test_leave_all_true(self):
        '''所有参数正确'''
        payload = {"WorkFlowCC":[],
                   "ImagesList":[],
                   "Data":{
                       "DeptID":"96f75a51-779b-491a-9773-cb5f90cef11e",
                       "DeptName":"技术研发部",
                       "PayDetailList":[
                           {"Amount":"2",
                            "Type":"差旅费",
                            "Statement":"报销"
                            }
                       ]
                   }
                   }
        r = requests.post(self.base_url,json = payload,cookies = self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['Success'],True)
    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
