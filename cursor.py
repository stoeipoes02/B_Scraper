import mariadb
import sys

try:
    conn = mariadb.connect(
        user="exampleuser",
        password="kick",
        host="localhost",
        database="example"
    )

except mariadb.Error as e:
    print(f'Error connecting to mariadb platform: {e}')
    sys.exit(1)

cur = conn.cursor()


cur.execute(
    "SELECT username FROM users")

for username in cur:
    print(f"first name: {username[0]}")
