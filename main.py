from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Миссия Колонизация Марса"


@app.route("/index")
def countdown():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return '</br>'.join([i for i in ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                                     'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                                     'Присоединяйся!']])


@app.route("/image_mars")
def image_mars():
    return "<title>Привет, Марс!</title><h1>Жди нас, Марс!</h1>" + \
           f'''<img src="https://www.barista-ltd.ru/components/com_jshopping/files/img_products/chocobar_Mars_50g.jpg"
           alt="здесь должна была быть картинка, но не нашлась">''' + '</br>Вот она какая, красная планета'


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
