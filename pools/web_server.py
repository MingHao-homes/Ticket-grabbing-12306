from settings import WebServer
from selenium import webdriver


def init_webdrive():
    webdriver_obj = None
    if WebServer == 1:
        webdriver_obj = webdriver.Chrome('chromedriver.exe')
    elif WebServer == 2:
        webdriver_obj = webdriver.Ie('../pools/IEDriverServer.exe')
    return webdriver_obj
    return webdriver

