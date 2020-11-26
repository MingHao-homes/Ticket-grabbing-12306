import sys
import random
import time
from settings import username, password, WebServer
from pools.YZMData import get_result
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 登录接口  login-api
class Login(object):
    def __init__(self):
        """
        实例化登录对象
        """
        self.webdriver = self.init_webdriver()
        # self.webdriver.maximize_window()
        if self.webdriver is None:
            sys.exit()

    def init_webdriver(self):
        """
        初始化驱动程序
        :return: None
        """
        webdriver_obj = None
        try:
            if WebServer == 1:
                webdriver_obj = webdriver.Chrome('../pools/chromedriver.exe',)
                webdriver_obj.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
                })
            elif WebServer == 2:
                webdriver_obj = webdriver.Edge('msedgedriver.exe')
            print('驱动加载成功!')
        except:
            print('启动加载失败，请检查配置游览器驱动')
            sys.exit()
        finally:
            return webdriver_obj

    def login(self):
        """
        实现登录操作
        :return: cookies
        """
        login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.webdriver.get(login_url)
        # 点击账号登录标签
        time.sleep(1)
        self.xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
        # 处理验证码
        self.check_yzm()
        # 输入账号密码
        self.xpath('//*[@id="J-userName"]').send_keys(username)
        self.xpath('//*[@id="J-password"]').send_keys(password)
        # 点击登录
        self.xpath('//*[@id="J-login"]').click()
        # 处理滑动验证码
        self.hd_yzm()
        # 获取登录之后的cookie
        self.get_cookies()

    def check_yzm(self):
        """
        处理验证码
        :return: None
        """
        try:
            # 截屏
            self.webdriver.save_screenshot('main.png')  # 截取的是当前完整的页面图片
            # 获取验证码图片左下角和右上角两点坐标
            img_tag = self.webdriver.find_element_by_xpath('//*[@id="J-loginImg"]')
            # 左下角坐标
            location = img_tag.location
            # 返回验证码图片的尺寸
            size = img_tag.size
            # 指定裁剪的范围
            rangle = (
                int(location['x']), int(location['y']), int(location['x'] + size['width']),
                int(location['y'] + size['height']))
            i = Image.open('./main.png')
            frame = i.crop(rangle)  # 根据裁剪的范围进行裁剪
            frame.save('code.png')
            # 验证码识别，返回点击坐标
            result = get_result(img_dir='code.png')
            print(result)  #:x1,y1|x2,y2|x3,y3
            # 将result转换成[[x1,y1],[x2,y2]]
            all_list = []
            if '|' in result:
                list_1 = result.split('|')
                count_1 = len(list_1)
                for i in range(count_1):
                    xy_list = []
                    x = int(list_1[i].split(',')[0])
                    y = int(list_1[i].split(',')[1])
                    xy_list.append(x)
                    xy_list.append(y)
                    all_list.append(xy_list)
            else:
                x = int(result.split(',')[0])
                y = int(result.split(',')[1])
                xy_list = []
                xy_list.append(x)
                xy_list.append(y)
                all_list.append(xy_list)

            for loc in all_list:
                x = loc[0]
                y = loc[1]
                ActionChains(self.webdriver).move_to_element_with_offset(img_tag, x, y).click().perform()
        except:
            print('处理登录验证码失败')
            sys.exit()

    def xpath(self, xpath_bas):
        """
        隐式等待进行xpath定位
        :param xpath_bas: xpath表达式
        :return: element
        """
        element = WebDriverWait(self.webdriver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_bas))
        )
        if element is None:
            print('出现未知错误，请下载最新代码!')
            sys.exit()
        return element

    def hd_yzm(self):
        """
        处理滑动验证码
        :return:
        """
        try:
            # 定位滑动验证位置
            res = self.xpath('//*[@id="nc_1_n1z"]')
            # 使用鼠标动作链进行点击并悬浮
            ActionChains(self.webdriver).click_and_hold(on_element=res).perform()

            distance = 500
            x = 500
            # 拖动超过拼接位置8个距离
            distance += 8
            v = 0
            t = 0.2
            tracks = []
            current = 0
            mid = distance * 7 / 8
            while current < distance:
                if current < mid:
                    a = random.randint(2, 4)
                else:
                    a = -random.randint(3, 5)
                v0 = v
                s = v0 * t + 0.5 * a * (t ** 2)
                current += s
                tracks.append(round(s))
                v = v0 + a * t
            # 补回超过距离为10，可多次测试，自测误差，进行多补或少补
            x = [-2, -3, -3, -2]
            tracks += x
            # 开始移动，加速，减速，超过，拖回
            for x in tracks:
                ActionChains(self.webdriver).move_by_offset(xoffset=x, yoffset=random.randint(100, 200)).perform()
            time.sleep(1)
            ActionChains(self.webdriver).release(res).perform()
        except:
            print('处理滑动验证码失败')
            sys.exit()

    def get_cookies(self):
        print(self.webdriver.get_cookies())


if __name__ == '__main__':
    a = Login()
    a.login()