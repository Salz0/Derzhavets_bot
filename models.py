from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField(name="unknown")
    register_DateTime = fields.DatetimeField(auto_now_add=True)
    presence = fields.BooleanField(presence=False)


class Choice(Model):
    id = fields.IntField(pk=True)
    place_name = fields.TextField(place_name="")
    floor = fields.TextField(floor="")
    room = fields.TextField(room="")
    roommates = fields.TextField(roommates="")
    p_date = fields.DatetimeField()
    f_date = fields.DatetimeField()
    r_date = fields.DatetimeField()
    rm_date = fields.DatetimeField()
    Name = fields.TextField(Name="")


class Questions(Model):
    order_number = fields.IntField(pk=True, generated=True)
    name = fields.TextField(name="unknown")
    question = fields.TextField(default="empty")
    question_datetime = fields.DatetimeField(auto_now_add=True)


class Voting(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField(name="unknown")
    vote1 = fields.TextField()
    vote2 = fields.TextField()
    vote3 = fields.TextField()
    vote4 = fields.TextField()
    p_date = fields.DatetimeField()
    f_date = fields.DatetimeField()
    r_date = fields.DatetimeField()
    rm_date = fields.DatetimeField()
