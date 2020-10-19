import requests as req

url = "https://cn.bing.com/ttranslatev3?&IG=36930619ABC34969A1377296A9AA2102&IID=SERP.5392.5"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

def any2tag(text, lan):
    '''任何语言翻译成中文或者英文lan = 1: 中文 lan = 2: 英文'''
    to = {
        1: "zh-Hans",
        2: "en"
    }
    payload = {
        "fromLang": "auto-detect",
        "text": text,
        "to": to[lan]
    }
    resp = req.post(url, data = payload, headers = headers)
    result = resp.json()
    return result[0]['translations'][0]['text']

if __name__ == '__main__':
    ans = any2tag('你好，再见', 1)
    print(ans)