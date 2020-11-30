#!/usr/bin/python3
import pymysql

# Open database connection
db = pymysql.connect("localhost","cs307-group07","q6m527HgKJuLStZD","cs307-group07-DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


def query(query_string):
    global cursor
    cursor.execute(query_string)
    return cursor.fetchall()

def update(update_string):
    global cursor
    cursor.execute(update_string)
    