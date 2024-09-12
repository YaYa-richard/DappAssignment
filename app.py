from flask import Flask, render_template, request
import datetime
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/main', methods=["GET", "POST"])
def main():
    r = request.form.get("q")
    return render_template('main.html', r=r)

@app.route('/store_money', methods=["GET", "POST"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money', methods=["GET", "POST"])
def transfer_money():
    return render_template('transfer_money.html')

@app.route('/admin', methods=["GET", "POST"])
def admin():
    return render_template('admin.html')

@app.route('/viewDB', methods=["GET", "POST"])
def viewDB():
    return render_template('viewDB.html', r="No data to display.")

@app.route('/delDB', methods=["GET", "POST"])
def delDB():
    return render_template('deleteDB.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
