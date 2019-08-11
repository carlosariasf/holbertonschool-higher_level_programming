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
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id ASC;", (sys.argv[4],))
    rows = cur.fetchall()
    ls_items = []
    for row in rows:
        ls_items.append(row[0])
    print(", ".join(ls_items))
    cur.close()
    db.close()

if __name__ == "__main__":
    """ Prevent import """
    main()
