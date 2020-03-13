import datetime
import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec
from data import db_session
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now,
                                   nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now,
                                 nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)