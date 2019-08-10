#!/usr/bin/python3
"""Documentation python3"""


import MySQLdb
import sys


def main():
    '''Main Function'''
    if (len(sys.argv) == 5):
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
        cur = db.cursor()
        try:
            cur.execute("SELECT * FROM states\
                    WHERE name IN ('{}')\
                    ORDER BY states.id ASC;".format(sys.argv[4]))
            rows = cur.fetchall()
        except MySQLdb.Error as e:
            try:
                print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            except IndexError:
                print("MySQL Error: %s" % str(e))
        for row in rows:
            print(row)
        cur.close()
        db.close()

if __name__ == "__main__":
    '''Prevent import'''
    main()
