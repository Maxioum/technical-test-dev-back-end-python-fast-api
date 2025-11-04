from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_name: str = "back-fast-api"
    debug: bool = False
    db_user: str = ""
    db_password: str = ""
    db_name: str = "test.db"

    @property
    def db_url(self) -> str:
        return f"sqlite:///./{self.db_name}"


config = Config()
