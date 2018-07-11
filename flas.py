from flask import Flask 
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute("SELECT * FROM stocks")
    return c.fetchone()[0]
    
if __name__ == "__main__":
    app.run()