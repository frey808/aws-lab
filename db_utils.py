import pymysql
import os

def connect():
    return pymysql.connect(
        host='ff-db.cjpgvmytjpgy.us-east-2.rds.amazonaws.com',
        port=3306,
        user='sophiagallegos',
        password='vdmOkBp5Lq1#uRT8',
        database='FIERCEFASHION'
    )

def exec_sql_file(path): #might not work
    full_path = os.path.join(os.path.dirname(__file__), path)
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result