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


#cur.execute(
#    "SELECT username FROM users")

#for messages in cur:
#    print(f"first name: {username[0]}")

try:
    cur.execute("INSERT INTO messages (user_id, text, time) VALUES (1, 'hey', CURRENT_TIMESTAMP)")
    conn.commit() # commits transaction
    print("data inserted succesfully")

except mariadb.Error as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    conn.close()

