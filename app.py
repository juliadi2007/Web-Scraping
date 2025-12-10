from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


def tambah(x, y):
    return x + y

def filter_berita(media):
    element = ""
    medianya = ""

    if media == "kompas":
        element = "h1"
        medianya = "hlTitle"
    elif media == "detik":
        element = "h3"
        medianya = "list-content__title"
    
    return [element, medianya]

def ambil_data(media, url):
    ambil = requests.get(url)
    konten = BeautifulSoup(ambil.content, "html.parser")

    fltr = filter_berita(media)
    element, medianya = fltr[0], fltr[1]



    cari = konten.find(element, class_ = medianya)
    if cari :
        return cari.text
    else:
        return "data tidak ditemukan"


app = Flask(__name__, template_folder="web")

@app.route("/")

def home():
    # hasil = tambah(20,10)
    kompas = ambil_data("kompas", "https://www.kompas.com/")
    detik = ambil_data("detik", "https://www.detik.com/")
    return render_template("index.html", kompas=kompas, detik=detik)

if __name__ == "__main__":
    app.run(debug=True)
