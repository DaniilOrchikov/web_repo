import datetime
from flask import Flask
from data import db_session
from data.jobs import Job
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


def add_job(team_leader, job, work_size, collaborators, is_finished):
    new_job = Job()
    new_job.team_leader = team_leader
    new_job.job = job
    new_job.work_size = work_size
    new_job.collaborators = collaborators
    new_job.is_finished = is_finished
    db_sess = db_session.create_session()
    db_sess.add(new_job)
    db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    add_user('Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org')
    add_user('White', 'Max', 52, 'colonist', 'engineer', 'module_1', 'user_1@mars.org')
    add_user('Gray', 'Sasha', 19, 'colonist', 'engineer', 'module_1', 'user_2@mars.org')
    add_user('Green', 'Ben', 36, 'colonist', 'engineer', 'module_1', 'user_3@mars.org')
    add_job(1, 'deployment of residential modules 1 and 2', 15, '2, 3', False)
    # app.run()


if __name__ == '__main__':
    main()
