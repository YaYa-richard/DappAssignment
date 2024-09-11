from flask import Flask,render_template,request
import sqlite3
import datetime
import os

app=Flask(__name__)
# 数据库初始化函数
def init_db():
    with sqlite3.connect('dapp.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("Database initialized successfully.")
        conn.commit()

# @app.before_first_request
# def setup():
#     init_db()

@app.route('/',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/main',methods=["get","post"])
def main():
    r = request.form.get("q")
    if r:
        current_time = datetime.datetime.now()
        with sqlite3.connect('dapp.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO user (data, created_at) VALUES (?, ?)", (r, current_time))
            conn.commit()
    return render_template('main.html', r=r)

@app.route('/store_money',methods=["get","post"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money',methods=["get","post"])
def transfer_money():
    return render_template('transfer_money.html')

@app.route('/admin',methods=["get","post"])
def admin():
    return render_template('admin.html')

@app.route('/viewDB',methods=["get","post"])
def viewDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute("select * from user")
    r = ""
    for row in c:
        r += str(row) + "\n"
    conn.commit()
    c.close()
    conn.close()
    return render_template('viewDB.html',r=r)

@app.route('/delDB',methods=["get","post"])
def delDB():
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute("delete from user")
    conn.commit()
    c.close()
    conn.close()
    return render_template('deleteDB.html')

if __name__=='__main__':
    init_db()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
