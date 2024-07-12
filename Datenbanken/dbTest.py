import pymysql

db = pymysql.connect(host='i-mariadb-01.informatik.hs-ulm.de',
                     user='inf2_usr207',
                     passwd='nbdk48',
                     db='inf2_r_classic',
                     port=3306,
                     cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
i = 22
sql = 'SELECT * FROM Table WHERE id=%d' % i

cursor.execute(sql)
for row in cursor:
    print(row[0]+":", row[1])


cursor.close()
db.close()

