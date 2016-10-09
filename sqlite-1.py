import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(3213254231, '2016-01-02', 'Python', 8)")
    conn.commit() #need to run a commit whenever any update is made to a db
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db(): #runs a query that shows all data in our table
    c.execute('SELECT * FROM stuffToPlot WHERE value = 3 OR value = 7')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall(): #this prettys up the db in Python shell by printing every row separately
        print(row[0]) #prints only the first column [0] in the db


def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

##    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 8')
##    conn.commit()
##
##    c.execute('SELECT * FROM stuffToPlot')
##    [print(row) for row in c.fetchall()]

    

#alt + 3 will comment out selected text
##create_table()
###data_entry()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
##read_from_db()
##graph_data()
del_and_update()
c.close()
conn.close()
    
