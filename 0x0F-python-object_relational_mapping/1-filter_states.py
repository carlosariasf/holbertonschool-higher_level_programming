#!/usr/bin/pythonE
""" lists all states with a name starting with N (upper N) """
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
    cur.execute("SELECT * FROM states\
            WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    '''Prevent import'''
    main()
