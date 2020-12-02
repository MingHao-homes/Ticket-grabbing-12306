import os
import requests
from hashlib import md5
from settings import DM

HEADERS = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
}


def get_result(d_type=9004, img_dir='yzm.png'):
    if not os.path.exists(img_dir):
        return '处理验证码错误，请下载最新版本后重试'
    with open(img_dir, 'rb') as fp:
        img_info = fp.read()
    password = md5(DM['pwd'].encode('utf8')).hexdigest()
    base_params = {
        'user': DM['username'],
        'pass2': password,
        'softid': DM['app_id'],
    }
    params = {
        'codetype': d_type,
    }
    params.update(base_params)
    files = {'userfile': ('ccc.jpg', img_info)}
    r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=HEADERS)
    rest = r.json()
    return rest['pic_str']
