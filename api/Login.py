import random
import requests
from .constant import *

class Login(object):
    def __init__(self, username, password):
        """
        实例化登录对象
        :param username: 12306用户名
        :param password: 12306密码
        :param login_url: 登录的首页
        """
        self.username = username
        self.password = password
        self.session = self.Session('https://kyfw.12306.cn/otn/login/init')
        print(self.session.cookies)

    def get_yzm(self):
        """
        获取验证码
        :return: None
        """
        url = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
        params = {
            'login_site': 'E',
            'module': 'login',
            'rand': 'sjrand',
            str(random.random()): '',
        }
        img_data = self.session.get(url, params=params).content
        with open('yzm.png', 'wb') as fp:
            fp.write(img_data)
        print('下载验证码成功!')

    class Session(requests.Session):
        """
        继承requests的Session类，进行扩展和封装
        """
        def __init__(self, login_url):
            super().__init__()
            self.index = login_url
            # 获取初始化的cookles
            self.get(login_url, headers=HEADER)
            self.get('https://kyfw.12306.cn/passport/web/auth/uamtk', headers=HEADER)
            self.post('https://kyfw.12306.cn/passport/web/auth/uamtk', headers=HEADER, data={'appid': 'otn'})


if __name__ == '__main__':
    a = Login('1','2')
    a.get_yzm()