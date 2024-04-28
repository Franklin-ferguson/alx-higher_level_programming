#!/usr/bin/python3

import MySQLdb as mysqldb
from sys import argv

if __name__ == "__main__":

    mysqldb_connect = mysqldb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

    mysqldb_cursor = mysqldb_connect.cursor()

    mysqldb_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows = mysqldb_cursor.fetchall()

    for row in rows:
        print(row)

