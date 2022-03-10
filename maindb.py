from data import db_session
from flask import Flask
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
        print(user)

    for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user)
    # app.run()


if __name__ == '__main__':
    main()