import requests
# 导包调用URL
import app


class LoginApi:

    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login(self, mobile, password):
        """使用data来接收外部传入的mobile, password，拼接成要发送的数据""" 
        data = {"mobile": mobile, "password": password}
        # 发送登录请求并返回响应数据
        response = requests.post(self.login_url, json=data, headers=self.headers)

        return response
