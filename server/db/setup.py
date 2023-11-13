from server.db_utils import *

def rebuild():
    # exec_sql_file('db/schema.sql')
    # exec_sql_file('db/data.sql')
    exec_commit('DROP TABLE IF EXISTS test;')
    exec_commit('CREATE TABLE test(id SERIAL PRIMARY KEY, product TEXT);')
    exec_commit('INSERT INTO test(product) VALUES("ollie");')
