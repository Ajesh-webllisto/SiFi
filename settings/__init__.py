from decouple import config

from settings.base_settings import *

env = config("ENVIRONMENT")

if env == "DEV":
    from settings.dev_settings import *
elif env == "PROD":
    from settings.prod_settings import *
