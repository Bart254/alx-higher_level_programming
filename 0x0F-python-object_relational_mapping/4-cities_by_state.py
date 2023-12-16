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
    select = "SELECT cities.id, cities.name, states.name FROM cities"
    join = " JOIN states ON cities.state_id = states.id"
    order = " ORDER BY cities.id ASC"
    full_query = select + join + order
    cursor.execute(full_query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
