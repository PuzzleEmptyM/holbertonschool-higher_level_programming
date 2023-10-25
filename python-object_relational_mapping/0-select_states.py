#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to retrieve the states
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    # Fetch all the results
    states = cur.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cur.close()
    db.close()
