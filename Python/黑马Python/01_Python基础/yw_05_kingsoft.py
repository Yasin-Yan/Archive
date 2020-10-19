import requests as req

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
           "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=pnkR1YGsw5a7J4Ud_Cme6xB1KwgQb-2oxqZo9FgPaH7&wd=&eqid=e880865d00002804000000045f0ff3a5"}

def zh2en(text):
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
    payload = {
        "from": "auto",
        "to": "auto",
        "q": text
    }
    resp = req.post(url, data = payload, headers = headers)
    result = resp.json()
    return result['content']['out']

def en2zh(text):
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=c1ae2671a8801967'
    payload = {
        "from": "auto",
        "to": "zh",
        "q": text
    }
    resp = req.post(url, data = payload, headers = headers)
    result = resp.json()
    return result

if __name__ == '__main__':
    # ans = zh2en("胜利终将属于我们")
    ans = en2zh("I am iron man")
    print(ans)

