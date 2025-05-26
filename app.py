from flask import Flask, render_template, request, redirect, url_for
from scraper import scrape_books
from db import collection

app = Flask(__name__)

# Dummy login
USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
        return redirect(url_for('dashboard'))
    return "Invalid credentials", 403

@app.route('/dashboard')
def dashboard():
    data = list(collection.find({}, {'_id': 0}))
    return render_template('dashboard.html', books=data)

@app.route('/scrape')
def scrape():
    books = scrape_books()
    collection.delete_many({})
    collection.insert_many(books)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)















