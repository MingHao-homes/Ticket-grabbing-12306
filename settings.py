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

# 设置请求头
HEADERS = {
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

# 出发地
start_addr = "北京"
# 到达地
end_addr = "上海"
# 出发时间
start_time = '2020-12-04'  # 年月日必须按照年-月-日格式来写，月和日不足两位用零填充


