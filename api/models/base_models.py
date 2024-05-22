from peewee import Model

from config_db import db


class BaseModel_db(Model):

    class Meta:
        database = db