#!/usr/bin/python3
""" Connects python to Mysql using MYSQLdb to select specific items
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    db = MySQLdb.connect(host=host, user=usr, passwd=pwd, port=3306, db=db)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'\
            COLLATE utf8mb4_0900_bin".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
