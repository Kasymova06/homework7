import sqlite3
db = sqlite3.connect('txt.db')
a = db.cursor()
a.execute(""" CREATE TABLE IF NOT EXISTS user(
hobby text,
lastname text,
name text,
year_of_birth integer,
view integer
)
""");
# students = [
#     ('Zahro', 'Kasymova', 2006, 'Programming', 16),
#     ('Ayub', 'Rataruy', 2006, 'Photography', 9),
#     ('Abdulaziz', 'Aliev',2000, 'Music', 7),
#     ('Madison', 'Brak', 2002, 'Painting', 10),
#     ('Lenon', 'Smith', 2004, 'Reading', 10),
#     ('Jim', 'Parker', 2001, 'Singing', 6),
#     ('Zibo', 'Canton', 2008, 'Playing', 15),
#     ('Nena', 'Brown', 2006, 'Writing', 9),
#     ('Lily', 'Wilson', 2003, 'Dancing', 11),
#     ('Donald', 'Trump', 2009, 'Cooking', 9),
# ]

# for student in students:
#     a.execute("""
#     INSERT INTO user (name, lastname, year_of_birth, hobby, view)
#     VALUES (?,?,?,?,?)
#     """, student)

# a.execute("UPDATE user SET view = 'gunius' where view >= 10")

a.execute("SELECT * FROM user  Where view == 'gunius'")
item=a.fetchall()
for i in item:
    print(i)


a.execute("DELETE FROM user WHERE rowid % 2 == 0 ")
db.commit()
db.close()