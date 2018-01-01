#!/usr/bin/python3

# LOAD COMMON LIB
import sys
from lib.glas.glascore import gcore
from time import strftime, localtime

# 공통 라이브러리 실행
gc = gcore()

# 데이타베이스 연결 예제
con = gc.mysqlcon()


# 로깅 예제코드
gc.logger.info ("mysql connectcon")
gc.logger.critical ("Critical example")
gc.logger.debug ("debug example")
gc.logger.error ("error example")
gc.logger.warning ("warning example")

cursor = con.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()

#print ("SERVER VERSION :" ,row[0])

cursor.close()
con.close()

print(strftime("%Y", localtime()))

