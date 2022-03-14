from flask import Flask, url_for, render_template, request

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


@app.route("/promotion_image")
def promotion_image():
    return render_template('index.html', title='Домашняя страница')


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Пример формы</title>
</head>
<body>
<h1 align="center">Анкета претендента</h1>
<h3 align="center">на участие в миссии</h3>
<div>
    <form class="login_form" method="post">
        <input type="surname" class="form-control" id="surname"
               placeholder="Введите фамилию" name="surname">
        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
        <br>
        <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
        <div class="form-group">
            <label for="educationSelect">Какое у вас образование?</label>
            <select class="form-control" id="educationSelect" name="education">
                <option>Начальное</option>
                <option>Среднее</option>
                <option>Высшее</option>
            </select>
        </div>
        Какие у Вас есть профессии?
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check1" name="check1">
            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check2" name="check2">
            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check3" name="check3">
            <label class="form-check-label" for="acceptRules">Пилот</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check4" name="check4">
            <label class="form-check-label" for="acceptRules">Метеоролог</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check5" name="check5">
            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check6" name="check6">
            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check7" name="check7">
            <label class="form-check-label" for="acceptRules">Врач</label>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="check8" name="check8">
            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
        </div>
        <div class="form-group">
            <label for="about">Немного о себе</label>
            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <div class="form-group">
            <label for="form-check">Укажите пол</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
</div>
</body>
</html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
