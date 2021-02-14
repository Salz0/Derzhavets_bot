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
    p_date = fields.DatetimeField(auto_now=True)
    f_date = fields.DatetimeField(auto_now=True)
    r_date = fields.DatetimeField(auto_now=True)
    rm_date = fields.DatetimeField(auto_now=True)
    Name = fields.TextField(Name="")


class Questions(Model):
    order_number = fields.IntField(pk=True, generated=True)
    name = fields.TextField(name="unknown")
    question = fields.TextField(default="empty")
    question_datetime = fields.DatetimeField(auto_now_add=True)
