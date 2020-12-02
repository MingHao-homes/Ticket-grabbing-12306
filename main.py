import API_Class.Login as Login
from API_Class.Grabbing_Find import GrabbingFind

longin_obj = Login.Login()
cookie = longin_obj.login()

"""
[{"domain": "kyfw.12306.cn", "httpOnly": false, "name": "uKey", "path": "/", "secure": false, "value": "38616db1e63af439b23a290f0532d3b232ba32e045b2233638cefadc485d52a7"}, {"domain": ".12306.cn", "expiry": 1924905600, "httpOnly": false, "name": "RAIL_DEVICEID", "path": "/", "secure": false, "value": "FVytyBlEe3OzhPg1Z4hXqqPhYE9zUSpl3xUxjOCJE--hO6eEj_-62mt6DUgVlx8K5A1G8ef2_C98GvSlzUfs3bVQRZRyEU5GBp-mspYnKWu9LFmsJc_9IGHwF0ILdcrODSQrnb55GzxfKiEa0OO5k8fau6mwMdn6"}, {"domain": "kyfw.12306.cn", "httpOnly": false, "name": "BIGipServerpool_passport", "path": "/", "secure": false, "value": "98828810.50215.0000"}, {"domain": ".12306.cn", "expiry": 1693098484, "httpOnly": false, "name": "RAIL_EXPIRATION", "path": "/", "secure": false, "value": "1607001930666"}, {"domain": "kyfw.12306.cn", "httpOnly": false, "name": "route", "path": "/", "secure": false, "value": "c5c62a339e7744272a54643b3be5bf64"}, {"domain": "kyfw.12306.cn", "httpOnly": false, "name": "tk", "path": "/otn", "secure": false, "value": "DHsMil75iANqrLqIqSm0-4LztLvRQORf86mFOV5aRiomkQ1Q0"}, {"domain": "kyfw.12306.cn", "httpOnly": false, "name": "BIGipServerotn", "path": "/", "secure": false, "value": "468713994.64545.0000"}, {"domain": "kyfw.12306.cn", "httpOnly": false, "name": "JSESSIONID", "path": "/otn", "secure": false, "value": "38FB46F7AF6AC16C194631B6288D585A"}]
"""

print(GrabbingFind(cookie).get_ticket())

