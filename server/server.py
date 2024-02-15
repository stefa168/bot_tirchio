import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, Application


def load_api_key(path: str) -> str:
    with open(path, 'r') as f:
        return f.read().strip()


def main(api_key: str):
    application: Application = ApplicationBuilder().token(api_key).build()

    application.run_polling()


if __name__ == '__main__':
    _api_key_path: str = os.getenv('API_KEY_FILE') if os.getenv('API_KEY_FILE') is not None else "./api_key"
    _key = load_api_key(_api_key_path)

    # todo add global engine from SQLAlchemy

    # logging.basicConfig()
    # logging.getLogger("sqlalchemy-engine").setLevel(logging.INFO)

    main(_key)
