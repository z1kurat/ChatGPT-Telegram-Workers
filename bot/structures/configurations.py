import logging

from dataclasses import dataclass

from os import getenv

from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    """Database connection variables"""
    name: str = getenv("POSTGRES_DATABASE")
    user: str = getenv("POSTGRES_USER", "bot")
    passwd: str = getenv("POSTGRES_PASSWORD", None)
    port: int = int(getenv("POSTGRES_PORT", 5432))
    host: str = getenv("POSTGRES_HOST", "localhost")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_str(self) -> str:
        """
        This function build a connection string
        """
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class RedisConfig:
    """Redis connection variables"""
    user_db: str = int(getenv("REDIS_USER_DATABASE", 1))
    fsm_db: str = int(getenv("REDIS_FSM_DATABASE", 2))
    misc_db: str = int(getenv("REDIS_MISC_DATABASE", 3))
    host: str = getenv("REDIS_HOST", "localhost")
    port: int = int(getenv("REDIS_PORT", 6379))
    passwd: int = getenv("REDIS_PASSWORD")
    username: int = getenv("REDIS_USERNAME")
    state_ttl: int = getenv("REDIS_TTL_STATE", None)
    data_ttl: int = getenv("REDIS_TTL_DATA", None)


@dataclass
class BotConfig:
    """Bot configuration"""
    token: str = getenv("TELEGRAM_BOT_TOKEN")


@dataclass
class APIConfig:
    """Bot configuration"""
    open_ai_key: str = getenv("OPENAI_KEY")


@dataclass
class Configuration:
    """All in one configuration's class"""

    debug = bool(getenv("DEBUG"))
    logging_level = int(getenv("LOGGING_LEVEL", logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()
    api = APIConfig()


conf = Configuration()
