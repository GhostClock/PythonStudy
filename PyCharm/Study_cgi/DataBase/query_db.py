#!/usr/bin/python
# coding=utf-8

import pymysql

def query(db):
    cursor = db.cursor()

    sql = "select * from emplpyee where income > '%d'" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id      =   row[0]
            fname   =   row[1]
            lname   =   row[2]
            age     =   row[3]
            sex     =   row[4]
            income  =   row[5]

            print "id = %s fname = %s lname = %s age = %s  sex = %s income = %s" % (id,fname, lname, age,sex,income)
    except pymysql.Error as error:
        print error.message