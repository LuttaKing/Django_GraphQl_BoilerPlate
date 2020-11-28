from split_settings.tools import include

base_settings = [
    'components/common.py',
    'components/authentication.py',
    'components/database.py',
    'components/graphene.py',
    'components/heroku.py',
]

include(*base_settings)
