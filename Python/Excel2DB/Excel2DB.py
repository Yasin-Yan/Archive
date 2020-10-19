import pymysql.cursors
import openpyxl, pprint
from HomeSearch import homeSearch
from time import sleep

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='pydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print('打开工作簿...')
wb = openpyxl.load_workbook('2020届毕业生生源信息核查表.xlsx')
sheet = wb['计信学院']
count = 0

try:
	with connection.cursor() as cursor:
		sql = "INSERT INTO `student_test` (`student_id`, `name`, `department`, `professional`, `degree`, `id_card`, `classment`, `phone`, `email`, `go`, `sex`, `birth`, `home`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

		print('读取行...')
		for row in range(2, sheet.max_row + 1):
			student_id = sheet['A' + str(row)].value
			name = sheet['B' + str(row)].value
			department = sheet['C' + str(row)].value
			professional = sheet['D' + str(row)].value
			degree = sheet['E' + str(row)].value
			id_card = sheet['F' + str(row)].value
			classment = sheet['G' + str(row)].value
			phone = sheet['I' + str(row)].value
			email = sheet['J' + str(row)].value
			go = sheet['K' + str(row)].value
			
			#每存储10条数据暂停2秒
			# count += 1
			# if count % 10 == 0:
			# 	print("sleep...")
			# 	sleep(5)

			# 判断性别
			if len(str(id_card)) == 18:
				sex_str = str(id_card)[14:17]
				flag = int(sex_str) % 2
				if flag == 1:
					sex = '男'
				elif flag == 0:
					sex = '女'
				else:
					sex = '性别信息缺失'
				# 出生日期
				birth = str(id_card)[6:10] + '-' + str(id_card)[10:12] + '-' + str(id_card)[12:14]
				# 归属地
				home = homeSearch(str(id_card))
			print(str(student_id) + ' ' + str(name) + ' ' + str(department) + ' ' + str(professional) + ' ' + str(degree) + ' ' + str(id_card) + ' ' + str(classment) + ' ' + str(phone) + ' ' + str(email) + ' ' + ' ' + str(go) + ' '+ str(sex) + ' '+ birth + home + '\n')

			cursor.execute(sql, (str(student_id), str(name), str(department), str(professional), str(degree), str(id_card), str(classment), str(phone), str(email), str(go), sex, birth, home))
		# cursor.execute(sql, ('2019', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016'))
	connection.commit()
finally:
	connection.close()