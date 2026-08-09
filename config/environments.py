from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    """Перечень доступных окружений"""
    DEV = "dev"
    PROD = "prod"

    def __str__(self):
        return self.value


_URLS = {
    Environment.DEV: 'http://memesapi.course.qa-practice.com',
    Environment.PROD: 'http://memesapi.course.qa-practice.com',
}


class EnvironmentConfig(BaseSettings):
    """Конфиг окружения"""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    url: str
    token: str


def load_environment(env: Environment | str) -> EnvironmentConfig:
    """Возвращает конфиг для запрошенного окружения.
    URL берётся из статической таблицы _URLS, секреты — из .env / env vars.
    """
    env = env if isinstance(env, Environment) else Environment(env.lower())
    return EnvironmentConfig(url=_URLS[env])
