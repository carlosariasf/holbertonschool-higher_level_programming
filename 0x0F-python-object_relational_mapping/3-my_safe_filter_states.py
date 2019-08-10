#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import MySQLdb
import sys


def main():
    """ Main Function """
    if (len(sys.argv) == 5):
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY %s\
                ORDER BY states.id ASC;", (sys.argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()

if __name__ == "__main__":
    """ Prevent import """
    main()
