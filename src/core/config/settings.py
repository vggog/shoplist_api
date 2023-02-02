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
    POSTGRES_DB_TEST: str = env('POSTGRES_DB_TEST')
    DB_URL_TEST = str(
        f'postgresql+psycopg2://{POSTGRES_USER_NAME}:{POSTGRES_USER_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_TEST}'
    )

    # Redis settings
    REDIS_HOST: str = env('REDIS_HOST')
    REDIS_PORT: int = env('REDIS_PORT')
    DATA_RETENTION_TIME: int = 300

    #SMTP
    SMTP_LOGIN = env('SMTP_LOGIN')
    SMTP_PASSWORD = env('SMTP_PASSWORD')
    SMTP_HOST = env('SMTP_HOST')
    SMTP_PORT = env('SMTP_PORT')

