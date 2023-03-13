import flask
import sqlite3
import random
import os

class Titles:
    def __init__(self, filename):
        self.filename = filename
        req = "CREATE TABLE IF NOT EXISTS titles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)"
        conn = sqlite3.connect('titles.db')
        conn.execute(req)
        conn.commit()
        conn.close()

    def addTitle(self,title):
        conn = sqlite3.connect('titles.db')
        conn.execute("INSERT INTO titles (title) VALUES ('{}')".format(title))
        conn.commit()
        conn.close()

    def removeTitle(self,title):
        conn = sqlite3.connect('titles.db')
        conn.execute("DELETE FROM titles WHERE title = '{}'".format(title))
        conn.commit()
        conn.close()

    def getRandomTitle(self):
        conn = sqlite3.connect('titles.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM titles ORDER BY RANDOM() LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        return result
    
    def getTitles(self):
        conn = sqlite3.connect('titles.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM titles")
        result = cursor.fetchall()
        conn.close()
        return result
    
    def getTitlesCount(self):
        conn = sqlite3.connect('titles.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM titles")
        result = cursor.fetchone()
        conn.close()
        return result[0]
    
    def getTitlesList(self):
        conn = sqlite3.connect('titles.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM titles")
        result = cursor.fetchall()
        conn.close()
        return [x[0] for x in result]

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect(flask.url_for('control'))

@app.route('/control')
def control():
    return flask.render_template('control.html')

@app.route('/titles')
def titles():
    title = titles.getRandomTitle()
    print(title)
    return flask.render_template('title.html', title=title)

if __name__ == '__main__':
    titles = Titles('titles.db')
    titles.addTitle('test')
    titles.addTitle('test2')
    titles.addTitle('test3')
    titles.addTitle('test4')
    titles.addTitle('test5')
    app.run(debug=True)