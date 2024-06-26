#Import Libraries to be used through all the code
from flask import Flask, render_template
import sqlite3
import pathlib 

#Database location folder path/
#PLEASE: Update your device folder location where this repository was download/stored.
base_path = pathlib.Path(r"C:\Users\User")

#Database name where data frame was stored
db_name = "kobe.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    kobe = cursor.execute("SELECT * FROM kobe_table").fetchall()
    con.close()

    return render_template("data_table.html", kobe = kobe)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)