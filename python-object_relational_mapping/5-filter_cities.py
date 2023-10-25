#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
        "\
        SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id ASC\
        "
    )
    output = cur.fetchall()
    print(", ".join([item[1] for item in output if item[2] == argv[4]]))
    cur.close()
    db.close()
