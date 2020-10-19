# -*- coding: utf-8 -*-
'''调用js文件的模块'''
import execjs as js

def get_js():
    '''打开js文件'''
    f = open('yw_04_sign.js', 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr += line
        line = f.readline()
    return htmlstr

def generate_sign(a):
    js_str = get_js()
    ctx = js.compile(js_str)
    return ctx.call('e', a)

if __name__ == '__main__':
    tk = generate_sign('hello Mary here')
    print(tk)