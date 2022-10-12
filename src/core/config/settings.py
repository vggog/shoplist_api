import environ


env = environ.Env()
environ.Env.read_env()


class Config:

    # DB SETTINGS
    POSTGRES_HOST: str = env('POSTGRES_HOST')
    POSTGRES_USER_NAME: str = env('POSTGRES_USER')
    POSTGRES_USER_PASSWORD: str = env('POSTGRES_PASSWORD')
    POSTGRES_DB: str = env('POSTGRES_DB')
    POSTGRES_PORT: int = env('POSTGRES_PORT')

    # DB url for sqlalchemy
    DB_URL = str(
        f'postgresql+psycopg2://{POSTGRES_USER_NAME}:{POSTGRES_USER_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )
