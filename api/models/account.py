from .base_models import BaseModel_db
import peewee as p
from peewee import CharField


class Account(BaseModel_db):
    id = p.AutoField()
    name = CharField()
    nick = CharField()
    email = CharField()
    phone = CharField()
    address = CharField()
    referral_code = CharField()
    password = CharField()
    user_name = CharField()


    class Meta:
        db_table = 'account'