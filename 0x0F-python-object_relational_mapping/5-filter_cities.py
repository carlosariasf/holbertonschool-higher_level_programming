#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import MySQLdb
import sys


def main():
    """ Main Function """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC;", (sys.argv[4],))
    rows = cur.fetchall()
    i = 1
    for row in rows:
        if i < len(rows):
            print(row[0], end=", ")
            i += 1
        else:
            print(row[0])
    cur.close()
    db.close()

if __name__ == "__main__":
    """ Prevent import """
    main()
