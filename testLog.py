# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="cs307-group07@localhost",
        password="q6m527HgKJuLStZD",
        host="0.0.0.0",
        database="cs307-group07-DB"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("SELECT * FROM users")

# Print Result-set
for (user) in cur:
    print(user)