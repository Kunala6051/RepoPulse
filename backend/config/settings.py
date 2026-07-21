from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_url: str = ""
    anthropic_api_key: str = ""
    github_webhook_secret: str = ""
    database_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
