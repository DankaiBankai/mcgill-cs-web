#!/usr/bin/python3
import pymysql
import re
import random

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
    global db
    cursor.execute(update_string)
    db.commit()

def format_to_sql(string):
    string = re.sub(">\n", ">", string)
    string = re.sub("\n<", "<", string)
    return string

def format_to_user(string):
     string = re.sub(">", ">\n", string)
     string = re.sub("<", "\n<", string)
     return string

def checkCredentials(username, password):
    global cursor
    query = """SELECT username,password FROM users"""
    cursor.execute(query)
    data = cursor.fetchall()
    username_DB = data[0][0]
    password_DB = data[0][1]
    return (username_DB == username and password_DB == password)

def generateTicket(username):
    global cursor
    ticket = random.getrandbits(64)
    query = """UPDATE users SET ticket={0} WHERE username='{1}'"""
    query = query.format(ticket, username)
    print(query)
    cursor.execute(query)
    db.commit()
    return ticket



