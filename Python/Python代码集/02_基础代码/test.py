# -*- coding: UTF-8 -*-
import random

import sys
tips = print('--猜数字--\n')
generate = random.randint(1, 10)
while True:
	try:
		answer = int(input('请输入一个数字\n'))
		if answer < generate:
			print('猜小了\n')
		elif answer > generate:
			print('猜大了\n')
		else:
			print('恭喜你，猜对了!谜底是' + str(generate))
			sys.exit()
	except Exception:
		print('输入的不是数字格式哦!')