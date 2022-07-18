from dataclasses import dataclass
from pathlib import Path

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    locale_dir: str
    locale_domain: str
    moralis_api_token: str
    support_chat_id: int

@dataclass
class RedisConfig:
    host: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous
    redis: RedisConfig



def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        redis=RedisConfig(
            host=env.str('REDIS_HOST'),
        ),
        misc=Miscellaneous(
            locale_domain='testbot',
            locale_dir=Path(__file__).parent.parent / f"locales/",
            moralis_api_token=env.str('MORALIS_API_TOKEN'),
            support_chat_id=env.int('SUPPORT_CHAT_ID'),
        )
    )
