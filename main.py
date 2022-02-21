from flask import Flask, url_for, render_template

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
    return "<h1>Жди нас, Марс!</h1>" + "</br>" + \
           f'''<img src="{url_for('static', filename='img/mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">''' + '</br>Вот она какая, красная планета'


@app.route("/promotion_image")
def promotion_image():
    return render_template('index.html', title='Домашняя страница')


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
