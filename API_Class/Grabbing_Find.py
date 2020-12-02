import os
import sys
import json
import time
from urllib import parse
from settings import start_addr, start_time, end_addr,HEADERS
import requests


class GrabbingFind(object):
    def __init__(self, cookies):
        self.session = requests.Session()
        self.station = self.get_station()
        # self.session.cookies.get(**i)

    def get_station(self):
        """
        获取站点信息,校验地址
        :return:
        """

        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        # try:
        if not os.path.exists('station.json'):
            res_str = requests.get(url, headers=HEADERS).text.split('=')[-1].strip("'")
            res_dic = {}
            for i in res_str[1:].split('@'):
                res = i.split('|')
                res_dic.update({res[1]: res[2]})

            with open('station,json', 'w', encoding='utf-8') as fp:
                json.dump(res_dic, fp=fp, ensure_ascii=False)
        with open('station,json', 'r', encoding='utf-8') as fp:
            res_dic = json.load(fp=fp)
        # except:
        #     print('获取站点信息失败')
        #     sys.exit()
        if res_dic.get(start_addr) and res_dic.get(end_addr):
            self.from_station = res_dic.get(start_addr)
            self.end_station = res_dic.get(end_addr)
            print('校验出发地和目的地成功')
        else:
            print('校验出发地和目的地失败')
            sys.exit()
        return res_dic

    def get_ticket(self):
        """
        余票查询函数
        :return:
        """
        url = 'https://kyfw.12306.cn/otn/leftTicket/query'
        start_addr_str = "," + self.station[start_addr]
        end_addr_str = "," + self.station[end_addr]
        from_cookie = str(start_addr.encode('unicode_escape')).replace(r'\\', '%').strip(r"b'").strip("'") + str(
            parse.quote(start_addr_str))
        end_cookie = str(end_addr.encode('unicode_escape')).replace(r'\\', '%').strip(r"b'").strip("'") + parse.quote(
            end_addr_str)
        from_date = start_time
        save_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        cookie_mode = '_jc_save_fromStation={}; _jc_save_toStation={}; _jc_save_fromDate={}; _jc_save_toDate={}; _jc_save_wfdc_flag=dc'
        cookie = cookie_mode.format(from_cookie, end_cookie, from_date, save_date)
        params = {
            'leftTicketDTO.train_date': from_date,
            'leftTicketDTO.from_station': start_addr_str.strip(','),
            'leftTicketDTO.to_station': end_addr_str.strip(','),
            'purpose_codes': 'ADULT',
        }
        self.session.cookies.set("authentication", cookie)
        response = self.session.get(url, params=params, headers=HEADERS).json()
        for i in response['data']['result'][-1::]:
            c = i.split("|")
            num = len(c)
            for j in range(num):
                print(j+1, c[j])

if __name__ == '__main__':
    a = GrabbingFind('11')

    a.get_ticket()

    """
    4 T109   # 列车号
    9 20:05  # 出发时间
    10 11:00  # 到站时间
    11 14:55  # 出他时间
    5 BJP  # 出发地
    6 SHH  # 始发地
    7 BJP  # 出发地
    8 SHH  # 始发地
    """