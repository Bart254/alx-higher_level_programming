#!/usr/bin/python3
""" Connects python to Mysql using MYSQLdb to select specific items
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'
    db = MySQLdb.connect(host=host, user=usr, passwd=pwd, port=3306, db=db)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
