import os
import ssl
from pathlib import Path

from dotenv import load_dotenv
from tortoise import Tortoise, expand_db_url


def get_config():
    ctx = ssl.create_default_context(cafile='')
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Env vars are not loaded automatically when we run `aerich` commands, if so - we load them manually
    if not os.environ.get('DATABASE_URL'):
        load_dotenv(Path() / '.env', encoding='utf-8')

    db = expand_db_url(os.environ.get('DATABASE_URL'))
    db['credentials']['ssl'] = ctx

    config = {
        'connections': {
            'default': db
        },
        'apps': {
            'bot': {
                'models': [
                    'models',
                    'aerich.models',
                ],
                'default_connection': 'default',
            }
        },
    }
    return config


async def init():
    # Init database connection
    await Tortoise.init(config=get_config())
    # Generate the schema
    await Tortoise.generate_schemas()


async def shutdown():
    await Tortoise.close_connections()


# Used by aerich.ini
TORTOISE_ORM_CONFIG = get_config()
