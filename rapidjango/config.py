import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="rapidjango",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="rapidjango_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from rapidjango.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export rapidjango_KEY=value
export rapidjango_KEY="@int 42"
export rapidjango_KEY="@jinja {{ this.db.uri }}"
export rapidjango_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
rapidjango_ENV=production rapidjango run
```

Read more on https://dynaconf.com
"""
