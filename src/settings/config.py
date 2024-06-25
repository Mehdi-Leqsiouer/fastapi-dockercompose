""" Configure settings
"""


from pydantic import BaseSettings


class Settings(BaseSettings):
    """Load all fields listed below from Environment Variables.
    If they not exist they will be taken from .env file.
    https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # postgres
    postgres_user: str
    postgres_password: str
    postgres_db: str
    pgport: int
    database_host: str
    postgres_db_schema: str = "public"

    # Environment
    current_environment: str = "DEV"


settings = Settings()
