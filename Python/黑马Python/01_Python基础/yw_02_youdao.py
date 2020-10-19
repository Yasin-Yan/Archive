import requests as req

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

def any2han(text):
   '''任意语言翻译成中文'''
   payload = {
        "i": text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15918427825949",
        "sign": "78bca0515a7a8672a0a52386963c10fe",
        "ts": "1591842782594",
        "bv": "a9c3483a52d7863608142cc3f302a0ba",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
   resp = req.post(url, data = payload, headers = headers)
   result = resp.json()
   return result['translateResult'][0][0]['tgt']

def any2en(text):
    '''任意语言翻译成英文'''
    payload = {
        "i": text,
        "from": "AUTO",
        "to": "en",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15918427825949",
        "sign": "78bca0515a7a8672a0a52386963c10fe",
        "ts": "1591842782594",
        "bv": "a9c3483a52d7863608142cc3f302a0ba",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    resp = req.post(url, data = payload, headers = headers)
    result = resp.json()
    return result['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    # ans = any2han("hello China")
    ans = any2en("你好，再见")
    print(ans)