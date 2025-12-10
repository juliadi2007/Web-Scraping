from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


def tambah(x, y):
    return x + y

def ambil_data():
    url = "https://www.kompas.com/"
    ambil = requests.get(url)
    konten = BeautifulSoup(ambil.content, "html.parser")
    cari = konten.find("h1", class_ = "hlTitle")
    if cari :
        return cari.text
    else:
        return "data tidak ditemukan"


app = Flask(__name__, template_folder="web")

@app.route("/")

def home():
    # hasil = tambah(20,10)
    data = ambil_data()
    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)
