import unittest, logging
from api.login_api import LoginApi
from utils import assert_common


class TestHRMLLogin(unittest.TestCase):

    def setUp(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("登录成功接口返回的数据为：{}".format(jsonData))

        # self.assertEqual(200,response.status_code) # 断言响应状态码
        # self.assertEqual(True,jsonData.get("success")) # 断言success的值
        # self.assertEqual(10000,jsonData.get("code")) # 断言code的值
        # self.assertIn("操作成功",jsonData.get("message")) # 断言message的值

        assert_common(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login('13900000002', '123456')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("账号不存在时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_is_exist(self):
        # 调用封装的登录接
        response = self.login_api.login('13800000002', 'error')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("密码错误时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_str(self):
        # 调用封装的登录接
        response = self.login_api.login('1380000000#', '123456')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("账号输入特殊字符时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_n(self):
        # 调用封装的登录接
        response = self.login_api.login('','error')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("账号为空时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_n(self):
        # 调用封装的登录接
        response = self.login_api.login('13800000002', '')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("密码为空时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_chin(self):
        # 调用封装的登录接
        response = self.login_api.login('1380000000在','123456')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("账号有中文时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_k(self):
        # 调用封装的登录接
        response = self.login_api.login('1380000 002','123456')

        # 接收返回的数据
        jsonData = response.json()
        # 调式输出登录接口返回的数据
        logging.info("账号有空格时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

        
