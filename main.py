from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    add_user('Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org')
    add_user('White', 'Max', 52, 'colonist', 'engineer', 'module_1', 'user_1@mars.org')
    add_user('Gray', 'Sasha', 19, 'colonist', 'engineer', 'module_1', 'user_2@mars.org')
    add_user('Green', 'Ben', 36, 'colonist', 'engineer', 'module_1', 'user_3@mars.org')
    # app.run()


if __name__ == '__main__':
    main()