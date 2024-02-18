import hashlib
import mariadb

def insert_exampledatabase_users(user_id, username, first_name, last_name, e_mail, password):
    try:
        conn = mariadb.connect(
            user="exampleuser",
            password="kick",
            host="localhost",
            database="PoC"
        )
        cur = conn.cursor()

        # Check if the user already exists
        cur.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        existing_user = cur.fetchone()

        if not existing_user:
            # User does not exist, insert the new user without specifying user_id
            cur.execute("INSERT INTO users (user_id, username, first_name, last_name, e_mail, password) VALUES (?, ?, ?, ?, ?, ?)", (user_id, username, first_name, last_name, e_mail, password))
            conn.commit()

    except mariadb.Error as e:
        print(f"Error inserting user: {e}")
        conn.rollback()

    finally:
        conn.close()

usernames = ['jsmith', 'rjones', 'jtaylor', 'mbrown', 'dwilliams', 'wwilson', 'Rjohnson', 'Jdavies', 'Tpatel', 'Crobinson']
first_names = ["james", "robert", "john", "michael", "david", "william", "Richard", "Joseph", "Thomas", "Charles"]
last_names = ["smith", "jones", "taylor", "brown", "williams", "wilson", "johnson", "davies", "patel", "robinson"]
e_mails = ['jamessmith@gmail.com', 'robertjones@gmail.com', 'johntaylor@gmail.com', 'michaelbrown@gmail.com', 'davidwilliams@gmail.com', 'williamwilson@gmail.com', 'Richardjohnson@gmail.com', 'Josephdavies@gmail.com', 'Thomaspatel@gmail.com', 'Charlesrobinson@gmail.com']
passwords = ['a17631f92aaa9a2d80d6fede40f33197', 'd572c6c76553f71431df7f585ec37010', '9a1d55d5bb77a6a16ba42cfb2ef3d5ec', 'bfb93a5625054401fea72aeb1ae9ec8d', '721fd9737be60a7496d1c8ab6d3a0cf9', '29cd75fa4fba6383594306c142e54c64', '002ee12ebee5f56103abdbaede9a848e', 'a21b1b50ec7252e496ecc26ef0947958', '70afb8df4928e8871ff40e686de5aaed', 'f23099beeec8a62bcab0e44e55ff7a02']

for i in range(len(usernames)):
    try:
        # Generate a unique user_id, you may need to adapt this based on your requirements
        user_id = i + 1
        insert_exampledatabase_users(user_id, usernames[i], first_names[i], last_names[i], e_mails[i], passwords[i])
    except mariadb.Error as e:
        print(f"Error inserting user: {e}")
