import requests as req
import yw_03_js as js

def any2han(text):
    '''任何语言翻译成中文'''
    url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&otf=2&ssel=0&tsel=0&xid=45662847&kc=3&tk=' + str(js.get_tk(text)) + '&q=' + str(text)

    resp = req.get(url)
    result = resp.json()
    return result[0][0][0]

def any2en(text):
    '''任何语言翻译成英语'''
    url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&dt=gt&otf=2&ssel=0&tsel=4&xid=45662847&kc=1&tk=' + str(js.get_tk(text)) + '&q=' + str(text)
    resp = req.get(url)
    result = resp.json()
    return result[0][0][0]

if __name__ == '__main__':
    # ans = any2han("check out")
    ans = any2en('你好，再见')
    print(ans)