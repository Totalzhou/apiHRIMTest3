import requests
import app


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 注意：如果我们调用员工管理模块的相关接口时，先调用login.py接口
        # 获取到的app.HEADERS 才会是令牌的格式
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        """封装添加员工接口"""
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-07",
            "formOfEmployment": 1,
            "workNumber": "67679879",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-29T16:00:00.000Z",
        }
        # 发送 添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    def query_emp(self):
        """封装查询员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        return requests.get(url, headers=self.headers)

    def modif_emp(self, username):
        """封装修改员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        data = {"username": username}
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        """封装删除员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        # 调用删除的http接口并返回响应数据
        return requests.delete(url,headers = self.headers)

