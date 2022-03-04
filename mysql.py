import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='shuvo',password='1234')
my_cursor = mydb.cursor()
my_cursor.execute('Show databases')
for i in my_cursor:
    print(i)