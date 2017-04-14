# -*- coding: UTF-8 -*-

# import socket
# import os
# SIZE = 1024

# for dirPath, dirNames, fileNames in os.walk("media"):
#     for f in fileNames:
#         if '.txt' in f:
#             print os.path.join(dirPath, f)

# def trans():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect(('127.0.0.1', 9999))
#     print s.recv(SIZE)
#     s.send('begin to send')
#     print 'sending, please wait for a second ...'
#     with open('media/test.txt', 'rb') as f:
#         for data in f:
#             s.send(data)
#     print 'sended !'
#     s.close()
#     print 'connection closed'


import MySQLdb
import os
import time


values = []

def OK(data,fname):
    i = 0
    db = MySQLdb.connect(host="140.134.25.198", user="factory", passwd="UrbnJ64XdHaDHhTq", db="factory",charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO fa_temperature(time,T1,G1,T2,G2,T3,G3,T4,T5,T6,H1,H2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for n in data:
        data2= (str(float(data[i][0])+time.time()), data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10], data[i][11])
        i = i+1
        cursor.execute(sql,data2) 
    db.commit()
    db.close()
    print str(fname)+'____ok'
    values = []
    os.rename(fname, fname.replace('.txt', '_OK.txt'))
def main():
    for dirPath, dirNames, fileNames in os.walk("media"):
        for f in fileNames:
            if '.txt' in f and '_OK.txt' not in f:
                x =  os.path.join(dirPath, f)
                with open(os.path.join(dirPath, f)) as f:
                    for line in f:
                        values.append([n for n in line.strip().split()])
                OK(values,x)
    time.sleep( 10 )
    main()
main()


