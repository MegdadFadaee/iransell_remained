import json
from tkinter import messagebox


class Url:
    BASE: str = 'https://my.irancell.ir'
    ADD_SESSIONS: str = '/sessions/add'
    TOKEN: str = '/api/authorization/v1/token'
    ACCOUNT: str = '/api/sim/v3/account'

    @staticmethod
    def post_token() -> str:
        return Url.BASE + Url.TOKEN

    @staticmethod
    def get_account() -> str:
        return Url.BASE + Url.ACCOUNT


try:
    config: str = open('config.json').read()
    config: dict = json.loads(config)
    token = config['token']
    interval = int(config['interval']) or 10000
except FileNotFoundError:
    messagebox.showerror('Config Not Found!', 'Config file Not Found!')
    exit(0)
except KeyError:
    messagebox.showerror('Token Not Found!', 'Token Not Found!')
    exit(0)

headers = {
    'Accept-Language': 'fa',
    'Authorization': token,
}
