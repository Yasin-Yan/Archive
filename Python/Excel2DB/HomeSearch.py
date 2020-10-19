import requests as req
import re

url = 'http://www.21cbi.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
"Cookie": "UM_distinctid=1751b6cca50386-0be694cafc4285-4313f6a-144000-1751b6cca513b7; bdshare_firstime=1602482916180; __gads=ID=247d83499b0319d4:T=1602482914:S=ALNI_Mb1FEvxC5Mzt_4Zl_QLR907qWKSqg; Hm_lvt_1601dfdebac1029b2ecf902e3a7717a3=1602482916; CNZZDATA1260629335=1424039133-1602480290-null%7C1602486936; Hm_lpvt_1601dfdebac1029b2ecf902e3a7717a3=1602487462"}

def homeSearch(id):
	payload = {
	"id": id
	}
	resp = req.post(url, data = payload, headers = headers)
	pattern = r'发证地：(.+?)\n\t\t\t\t\t\t<p">'
	# re.S标志使得.可匹配换行符
	result = re.findall(pattern, resp.content.decode('utf-8'), re.S)
	if len(result) > 0:
		return result[0]
	else:
		return ''

if __name__ == '__main__':
	result = homeSearch('421125199608183013')
	print(result)