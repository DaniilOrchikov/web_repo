from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/<int:number>")
def index(number):
    params = {'number': number,
              'title': 'Нумбер'
    }
    return render_template("index.html", **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
