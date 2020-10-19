import yw_01_bing as bing
import yw_02_youdao as youdao
import yw_03_google as google
import yw_04_baidu as baidu
import yw_05_kingsoft as kingsoft

print('Welcome to use unionfanyi v2.0, enter / to exit...')
while True:
    write = input('---------->')
    if write == '/':
        break
    elif write == '//':
        print('Powered by Yasin@2020.10.19, know more about the author please visit https://github.com/Yasin-Yan.')
    elif write[0] >= 'A' and write[0] <= 'z':
        print('Bing------->' + bing.any2tag(write, 1))
        print('YouDao----->' + youdao.any2han(write))
        print('Google----->' + google.any2han(write))
        print('Baidu------>' + baidu.en2zh(write))
        # print("KingSoft--->" + kingsoft.en2zh(write))
    else:
        print('Bing------->' + bing.any2tag(write, 2))
        print('YouDao----->' + youdao.any2en(write))
        print('Google----->' + google.any2en(write))
        print('Baidu------>' + baidu.zh2en(write))
        # print("KingSoft--->" + kingsoft.zh2en(write))

