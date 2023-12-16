#!/usr/bin/python3
""" Module uses MySQLdb to create a script
"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'
    db = MySQLdb.connect(host=host, user=usr, passwd=pwd, port=3306, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
