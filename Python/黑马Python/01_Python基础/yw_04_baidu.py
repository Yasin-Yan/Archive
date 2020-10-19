import requests as req
import yw_04_js as js

headers1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "cookie": "BIDUPSID=FBFC4832759F494D0583C58A92AD0E14; PSTM=1589525220; BAIDUID=FBFC4832759F494D517155CED3D97A9F:FG=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-271%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; BDSFRCVID=BdLOJeC62CVemuOrW-qkMWyXnA6xY1nTH6ao7fCSw2Jnjh-2WQAbEG0PSf8g0KubhaS4ogKKLgOTHPPF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJPDVI82JCD3j-5cbjAWq4tehHRGKU79WDTm_DonQJ5Vfq743IcaMUui2J7X365OyR6X-pPKKRAbelOb5T5kh4IJqH5UQxoa3mkjbUODfn02OP5PM-Q6j-4syPRrKMRnWNRTKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCcjqR8ZDj_aD65P; delPer=0; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1593143863,1593218528,1593953997,1594383578; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1594383578; __yjsv5_shitong=1.0_7_8fb9830e7e6884134ce67167a99d351dea46_300_1594383577849_117.150.176.161_f1bf7c1c; yjs_js_security_passport=b8caf4fad98684fdf63a8739f4a06270932f15ce_1594383578_js"}

headers2 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "cookie": "BIDUPSID=FBFC4832759F494D0583C58A92AD0E14; PSTM=1589525220; BAIDUID=FBFC4832759F494D517155CED3D97A9F:FG=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-271%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; BDSFRCVID=BdLOJeC62CVemuOrW-qkMWyXnA6xY1nTH6ao7fCSw2Jnjh-2WQAbEG0PSf8g0KubhaS4ogKKLgOTHPPF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJPDVI82JCD3j-5cbjAWq4tehHRGKU79WDTm_DonQJ5Vfq743IcaMUui2J7X365OyR6X-pPKKRAbelOb5T5kh4IJqH5UQxoa3mkjbUODfn02OP5PM-Q6j-4syPRrKMRnWNRTKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCcjqR8ZDj_aD65P; delPer=0; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1593143863,1593218528,1593953997,1594383578; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1594383578; __yjsv5_shitong=1.0_7_8fb9830e7e6884134ce67167a99d351dea46_300_1594383577849_117.150.176.161_f1bf7c1c; yjs_js_security_passport=b8caf4fad98684fdf63a8739f4a06270932f15ce_1594383578_js; BDRCVFR[VXHUG3ZuJnT]=mk3SLVN4HKm"
}

def en2zh(text):
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    payload = {
        "from": "en",
        "to": "zh",
        "query": text,
        "transtype": "realtime",
        "simple_means_flag": 3,
        "sign": js.generate_sign(text),
        "token": "d04ae49f31336712af505f8860d8b96b",
        "domain": "common"
    }
    resp = req.post(url, data=payload, headers = headers1)
    result = resp.json()
    return result['trans_result']['data'][0]['dst']

def zh2en(text):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    payload = {
        "from": "zh",
        "to": "en",
        "query": text,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": js.generate_sign(text),
        "token": "d04ae49f31336712af505f8860d8b96b",
        "domain": "common"
    }
    resp = req.post(url, data=payload, headers = headers2)
    result = resp.json()
    return result['trans_result']['data'][0]['dst']

if __name__ == '__main__':
    result = en2zh("hello Mary")
    # result = zh2en("你好玛利亚")
    print(result)



