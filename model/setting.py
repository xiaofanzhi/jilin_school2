import pymysql

#连接数据库

try:
    db = pymysql.connect(host="111.116.20.92",user="ccut",
        passwd="ccut",
        db="ccut1",
        charset='utf8')
except:
    print("could not connect to mysql server")