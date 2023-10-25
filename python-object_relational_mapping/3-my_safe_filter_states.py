#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa with name matching input
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states ORDER BY states.id ASC"
    )
    output = cur.fetchall()
    [print(item) for item in output if item[1] == argv[4]]
    cur.close()
    db.close()
