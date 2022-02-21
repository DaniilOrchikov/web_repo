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
    return "<h1>Жди нас, Марс!</h1>" + "</br>" + \
           f'''<img src="{url_for('static', filename='img/mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">''' + '</br>Вот она какая, красная планета'


@app.route("/promotion_image")
def promotion_image():
    return '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">''' + "<h1>Жди нас, Марс!</h1>" + "</br>" + \
           f'''<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
           <img src="{url_for('static', filename='img/mars.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">''' + '''<div class="alert alert-secondary" role="alert">
  Человечество вырастает из детства
</div>''' + '''<div class="alert alert-success" role="alert">
  Человечеству мала одна планета
</div>''' + '''<div class="alert alert-secondary" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты
</div>''' + '''<div class="alert alert-warning" role="alert">
  И начнем с Марса!
</div>''' + '''<div class="alert alert-danger" role="alert">
  Присоединяйся!
</div>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
