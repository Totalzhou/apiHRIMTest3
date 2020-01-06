import logging
import unittest
import app
import pymysql
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data, \
    DBUtils
from parameterized.parameterized import parameterized

app.EMP = 0


class TestIHRMEmp(unittest.TestCase):
    def setUp(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化员工表
        cls.emp_api = EmpApi()

    def tearDown(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        """调用添加员工接口"""
        response = self.emp_api.add_emp(username, mobile)
        # 获取添加员工接口的json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("添加员工接口返回的数据为:{}".format(jsonData))

        # 获取员工ID保存到全局变量
        app.EMP_ID = jsonData.get("data").get("id")
        logging.info("员工ID:{}".format(app.EMP_ID))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 获取查询员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("查询员工接口的返回数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self, username, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.modif_emp(username)
        # 获取查询员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("修改员工接口的返回数据为：{}".format(jsonData))
        # 建立连接

        with DBUtils() as db_utils:
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            # logging.info(db_utils.fetchone())
            db_utils.execute(sql)

            result = db_utils.fetchone()[0]
            logging.info("从数据库中查询的员工用户名是：{}".format(result))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, success, code, message, http_code):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        # 获取查询员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("删除员工接口的返回数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)
