from server.db_utils import *

def rebuild():
    exec_sql_file('db/schema.sql')
    exec_sql_file('db/data.sql')
