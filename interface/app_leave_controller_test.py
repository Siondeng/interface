import unittest
import requests
import time
import datetime
import get_cookie

class LeaveController(unittest.TestCase):
    '''请假'''
    def setUp(self):
        self.base_url = "http://qa.eipsev.com/ApplicationForLeave/SubmitApplicationForLeave"
        self.cookie = get_cookie.get_cookies()



    def test_leave_all_true(self):
        '''所有参数正确'''
        # 当前时间
        now = time.time()
        #一天后的时间
        onedayafter = (datetime.datetime.now() + datetime.timedelta(days = 1))
        onedayafter = int(time.mktime(onedayafter.timetuple()))
        #请假时长
        days = onedayafter - now
        payload = {
                    "WorkFlowCC": [],
                    "ImagesList": [],
                    "Data": {
                                "BeginTime": now,
                                 "Reason": "家中有事",
                                "DeptID": "96f75a51-779b-491a-9773-cb5f90cef11e",
                                 "Type": "af81ffe1-df67-468b-a94a-ae8a705e44c0",
                                "TypeName": "事假",
                                "EndTime": onedayafter,
                                "DeptName": "技术研发部",
                                "Days": days
                            }
                    }
        r = requests.post(self.base_url,json = payload,cookies = self.cookie)
        self.result = r.json()
        self.assertEqual(self.result['Success'],True)
    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
