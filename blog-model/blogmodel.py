
'''

Blog Model

Create a class to interface with sqlite3.  This type of object is typically called a Model.

The table in sqlite3 will have two columns: post_name and post_text

Discuss with your neighbour on how to solve this challenge.

To connect Python to SQL, reference the following:
http://www.pythoncentral.io/introduction-to-sqlite-in-python/

Your model should be able to:

1) Open a sqlite3 db connection
2) Close the connection
3) Create a new table with the correct fields
4) Perform CRUD actions on the database table

C - Create
R - Read
U - Update
D - Destroy

'''

import sqlite3

class BlogModel():
    def __init__(self,db_file):
        self.db_file = db_file

        self.post_name = None
        self.post_text = None

    def open(self):
        #"open sqlite3 db connection"
        # Creates or opens a file called mydb with a SQLite3 DB
        self.db = sqlite3.connect(self.db_file)

    def close(self):
        #"close the connection to sqlite3"
        self.db.close()

    def create_table(self):
        #create the table
        # Get a cursor object
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE blogcontent(id INTEGER PRIMARY KEY, post_name TEXT, post_text TEXT)
        ''')
        self.db.commit()

    def create(self, post_name, post_text):
        #create a new row with data that you pass in
        cursor = self.db.cursor()

        # Insert user 1
        cursor.execute('''INSERT INTO blogcontent(post_name, post_text )
                  VALUES(?,?)''', (post_name,post_text))
        print('First user inserted')

        self.db.commit()

    def read(self,id):
        # "search for id, and return post_name and post_text as a string"
        cursor = self.db.cursor()

        cursor.execute('''SELECT post_name, post_text FROM blogcontent WHERE id=?''', (id,))
        post = cursor.fetchone()
        print "Title:\n" + post[0] + "\n"
        print "Post Content:\n" + post[1]

    def update(self, id, post_name, post_text):
        cursor = self.db.cursor()

        # "search for id, and set a new post_name and post_text"
        cursor.execute('''UPDATE blogcontent SET post_name = ?, post_text = ? WHERE id=?''',
        (post_name, post_text, id))

        self.db.commit()

    def destroy(self,id):
        #"search for id, and delete that row"
        cursor = self.db.cursor()

        cursor.execute('''DELETE FROM blogcontent WHERE id = ? ''', (id,))
         
        self.db.commit()

blog = BlogModel("database.db")
blog.open()
#blog.create("Second Post", "All the words.")
#blog.read("1")
#blog.update("1","Firstest Post", "New content for things.")
blog.destroy("3")
