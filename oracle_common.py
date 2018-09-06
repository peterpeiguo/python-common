'''
pip install cx_Oracle
document: http://cx-oracle.readthedocs.io/en/latest/installation.html

tutorial:
http://www.oracle.com/technetwork/articles/dsl/python-091105.html
'''

from time import *
import cx_Oracle

def query_database(connection, query, condition): 
    cursor = connection.cursor()
    cursor.prepare(query)
    cursor.execute(None, condition)
    result = []
    for row in cursor:
        result.append(row)
    cursor.close()

    return result

def monitor(user, password, db, query, condition, initial_interval, adjustment_factor = 1.0):
    known_keys = {}
    interval = initial_interval
    while True:
        connection = cx_Oracle.connect(user, password, db)
        print(f"oracle version = {connection.version}")
        rows = query_database(connection, query, condition)
        connection.close()
        print(strftime("%H:%M", localtime()))
        empty = True
        for row in rows:
            if row[0] not in known_keys:
                empty = False
                print(row)
                known_keys[row[0]] = True
        if empty:
            interval *= adjustment_factor
        else:
            if interval > initial_interval:
                interval /= adjustment_factor
        print(interval)
        sleep(interval)
        print("=====================")        