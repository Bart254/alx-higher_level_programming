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
    select = "SELECT cities.name FROM cities"
    join = " JOIN states ON cities.state_id = states.id"
    where = " WHERE states.name = %s"
    order = " ORDER BY cities.id ASC"
    query = select + join + where + order
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for r in rows:
        for col in r:
            if r[-1] == col and rows[-1] == r:
                print(col)
            else:
                print(col, end=",")
