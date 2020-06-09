import pymysql.cursors
import openpyxl, pprint

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

try:
	with connection.cursor() as cursor:
		sql = "INSERT INTO `student` (`student_id`, `name`, `department`, `professional`, `degree`, `id_card`, `class`, `phone`, `email`, `go`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

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
			print(str(student_id) + ' ' + str(name) + ' ' + str(department) + ' ' + str(professional) + ' ' + str(degree) + ' ' + str(id_card) + ' ' + str(classment) + ' ' + str(phone) + ' ' + str(email) + ' ' + ' ' + str(go) + '\n')

			cursor.execute(sql, (str(student_id), str(name), str(department), str(professional), str(degree), str(id_card), str(classment), str(phone), str(email), str(go)))
		# cursor.execute(sql, ('2019', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016'))
	connection.commit()
finally:
	connection.close()
