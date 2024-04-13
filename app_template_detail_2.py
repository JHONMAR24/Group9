from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect("autos1.db")
    cursor = conn.cursor()
    auto = cursor.execute("SELECT * FROM auto").fetchall()
    conn.close()

    return render_template("data_table.html", auto=auto)

if __name__ == "__main__":
    app.run(debug=True)
