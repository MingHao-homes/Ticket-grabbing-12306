"""
请参考配置说明，修改配置文件，建议只修改12306的用户名和登录密码即可
Please refer to the configuration instructions to modify the
configuration file. It is recommended to only modify the
user name and login password of 12306
"""
import sys
import os

# 添加上一级目录运行环境
PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(PROJECT_DIR)

# 请求头配置  Request header configuration
HEADER = {
    'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

# 打码平台配置  Coding platform configuration
DM = {
    'username': 'xm123456',
    'pwd': '123456asd',
    'app_id': '910049',
}

# 设置驱动游览器
WebServer = 1  # 1是谷歌游览器，2是Edge游览器, 更多游览器正在添加中

# 12306账号设置：12306 username Settings
username = 'QF13864160882'

# 12306密码设置: 12306 password Settings
password = 'xm980526'

