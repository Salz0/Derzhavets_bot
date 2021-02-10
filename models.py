from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    register_DateTime = fields.DatetimeField(auto_now_add=True)

    # is_active = ''
    # profile = ''
    def __str__(self):
        return self.name


# if __name__ == "__main__":
#     run_async(init())