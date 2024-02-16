import hashlib
from cursor import insert_exampledatabase_users

usernames = []
first_name = ["james", "robert", "john", "michael", "david", "william", "Richard", "Joseph", "Thomas", "Charles"]
last_name = ["smith", "jones", "taylor", "brown", "williams", "wilson", "johnson", "davies", "patel", "robinson"]
e_mail = []
passwords = []


for first, last in zip(first_name, last_name):
    username = f"{first[0]}{last}"
    usernames.append(username)

    mail = f"{first}{last}@gmail.com"
    e_mail.append(mail)

    password = f"{first}{last}"
    hashed = hashlib.md5(password.encode()).hexdigest()
    passwords.append(hashed)


for user_id, (username, email, first, last, password) in enumerate(zip(usernames, e_mail, first_name, last_name, passwords), start=1):
    insert_exampledatabase_users(username, first, last, email, password)