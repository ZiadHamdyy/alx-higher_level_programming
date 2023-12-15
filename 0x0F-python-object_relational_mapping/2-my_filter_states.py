#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    if len(sys.argv) != 5:
        sys.exit(1)

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (args[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
