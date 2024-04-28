#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


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
        print("Error connecting to dabase: {}".forrmat(e))
        sys.exit(1)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
