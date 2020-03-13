from flask import Flask, render_template
from flask_login import LoginManager
from data import db_session
from data import users, jobs
import datetime

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.sqlite")
    app.run()


@app.route("/")
def log():
    session = db_session.create_session()
    jobbs = session.query(jobs.Jobs)
    team_leader = []
    for i in jobbs:
        leader = int(i.team_leader)
        team_leader += [session.query(users.User).filter(users.User.id == leader).first()]
    return render_template("log.html", jobs=jobbs, team_leader=team_leader)



@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)


if __name__ == '__main__':
    main()
