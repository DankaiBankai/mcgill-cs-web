#!/usr/bin/python3
import pymysql
import re
import random

# Open database connection
db = pymysql.connect("localhost","cs307-group07","q6m527HgKJuLStZD","cs307-group07-DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#Takes a SELECT query string as input and executes the query
def query(query_string):
    global cursor
    cursor.execute(query_string)
    return cursor.fetchall()

#Takes a UPDATE query string as input and executes the query
def update(update_string):
    global cursor
    global db
    cursor.execute(update_string)
    print("test")
    print(cursor._last_executed)
    db.commit()

#Removes newline characters before and after each tag
def format_to_sql(string):
    string = re.sub(">\n", ">", string)
    string = re.sub("\n<", "<", string)
    return string

#Adds newline characters before and after each tag for readability
def format_to_user(string):
     string = re.sub(">", ">\n", string)
     string = re.sub("<", "\n<", string)
     return string

#Verify credentials
def checkCredentials(username, password):
    global cursor
    query = """SELECT username,password FROM users"""
    cursor.execute(query)
    data = cursor.fetchall()
    username_DB = data[0][0]
    password_DB = data[0][1]
    return (username_DB == username and password_DB == password)

#Generate login ticket
def generateTicket(username):
    global cursor
    ticket = random.getrandbits(32)
    query = """UPDATE users SET ticket={0} WHERE username='{1}'"""
    query = query.format(ticket, username)
    cursor.execute(query)
    db.commit()
    return ticket

#Verify if ticket from users browser matches ticket in DB
def verify(ticket):
    global cursor
    query = """SELECT * FROM users WHERE ticket='{0}'"""
    query = query.format(ticket)
    cursor.execute(query)
    if (cursor.rowcount == 0):
        return "Fail"
    else:
        return "Success"



