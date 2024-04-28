#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=db_name,
                charset="utf8"
                )

    except MySQLdb.Error as e:
        print("Error connecting to database: ()".format(e))
        sys.exit(1)

    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                    states.id ASC".format(state_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
