import time
import unittest
import app
from soript.login import Login
from tools.HTMLTestRunner import HTMLTestRunner
from soript.test_emp import TestIHRMEmp

# 初始化测试套件
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))

# 使用HTMLtestRunner执行测试套件，生成测试报告
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:
    # 初始化HTMLtestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="V1.0.0")
    # 使用runner运行测试套件
    runner.run(suite)
