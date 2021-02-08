import os
from tortoise.models import Model
from tortoise import fields
from tortoise import Tortoise, run_async


# import psycopg2
# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')


class UserModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    register_DateTime = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url=os.environ.get('DATABASE_URL'),
        modules={"models": ["models"]}
    )
    # sql = get_schema_sql(Tortoise.get_connection("default"), safe=False)
    # print(sql)
    # Generate the schema
    await Tortoise.generate_schemas()


# run_async is a helper function to run simple async Tortoise scripts.
# run_async(init())

# # Create instance by save
# tournament = UserModel(name='New Tournament')
# await tournament.save()
#
# # Or by .create()
# await UserModel.create(name='Another Tournament')
#
# # Now search for a record
# tour = await UserModel.filter(name__contains='Another').first()
# print(tour.name)

if __name__ == "__main__":
    run_async(init())
