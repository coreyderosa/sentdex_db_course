#MySQL and Python tutorial-sentdex
#this may look incomplete.  This db was created on pythonanywhere.com and then queried via Python

import MySQLdb 
import time

#establishing the db connection.  This db is located on pythonanywhere.com
conn = MySQLdb.connect('binaryjoe01.mysql.pythonanywhere-services.com', 'binaryjoe01', 'F@tone28', 'binaryjoe01$MySql-1')

c = conn.cursor()

username = 'Python'
tweet = 'man im so cool'

#inserting the variables above in to the db
c.execute('INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)',
            (time.time(), username, tweet))

conn.commit()


c.execute('SELECT * FROM taula')

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)

conn.close()
