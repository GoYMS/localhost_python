"""
破解有道词典
"""
from urllib import request,parse
#key是要传入的参数
def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15631812641022",
        "sign": "a72d8ff983a32d972678c5eea4d1faf0",
        "ts": "1563181264102",
        "bv": "3a019e7d0dda4bcd253903675f2209a5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    #参数data必须是buytes类型
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Accept - Encoding":"gzip, deflate",
        "Accept - Language": "zh - CN, zh;q = 0.9",
        "Connection":" keep - alive",
        "Content - Length": "240",
        "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
        "Cookie": "OUTFOX_SEARCH_USER_ID = 907427277 @ 10.168.8.63;JSESSIONID = aaah6isUMYmeJ6vCo30Vw;OUTFOX_SEARCH_USER_ID_NCOO = 866866360.6675595;___rl__test__cookies = 1563181264098",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com /",
        "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36",
        "X - Requested - With": "XMLHttpRequest"
    }
    req = request.Request(url=url,data=data,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
if __name__ == '__main__':
    youdao("girl")
