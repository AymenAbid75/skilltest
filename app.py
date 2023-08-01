from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Fonction pour générer un raccourci aléatoire
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Redirection vers l'URL longue
@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('SELECT long_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()

    if result:
        long_url = result[0]
        return redirect(long_url)
    else:
        return "URL non trouvée."

# Générer un raccourci pour l'URL soumise
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()

    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO urls (short_url, long_url) VALUES (?, ?)', (short_url, long_url))
    conn.commit()
    conn.close()

    return render_template('shorten.html', short_url=short_url)

if __name__ == '__main__':
    # Créez une table pour stocker les URL si elle n'existe pas déjà
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS urls (short_url TEXT, long_url TEXT)')
    conn.close()

    app.run(debug=True)