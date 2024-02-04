import mariadb

def insert_user(user_id, username, first_name, last_name):
    try:
        conn = mariadb.connect(
            user="exampleuser",
            password="kick",
            host="localhost",
            database="example"
        )
        cur = conn.cursor()

        # Check if the user already exists
        cur.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        existing_user = cur.fetchone()

        if not existing_user:
            # User does not exist, insert the new user
            cur.execute("INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)", (user_id, username, first_name, last_name))
            conn.commit()

    except mariadb.Error as e:
        print(f"Error inserting user: {e}")
        conn.rollback()

    finally:
        conn.close()


def insert_message(user_id, text, type, username, first_name, last_name):
    try:
        conn = mariadb.connect(
            user="exampleuser",
            password="kick",
            host="localhost",
            database="example"
        )
        cur = conn.cursor()

        # Ensure user exists in the users table
        insert_user(user_id, username, first_name, last_name)  # You may want to replace "default_username" with the actual username logic

        # Insert message with the user_id
        cur.execute("INSERT INTO messages (user_id, text, time, type) VALUES (?, ?, CURRENT_TIMESTAMP, ?)", (user_id, text, type))
        conn.commit()

    except mariadb.Error as e:
        print(f"Error inserting message: {e}")
        conn.rollback()

    finally:
        conn.close()


