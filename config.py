import sys, json
from tkinter.messagebox import showerror


def error(title, text=None) -> None:
    if text is None:
        text = title

    showerror(title, text)
    sys.exit()


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


class Config:
    def __init__(self) -> None:
        try:
            with open('config.json') as file:
                config_file: str = file.read()
                configs: dict = json.loads(config_file)
                self.access_token = configs['access_token']
                self.payload = configs['payload']
                self.interval = int(configs['interval']) or 10000
        except FileNotFoundError:
            error('Configs Not Found!', 'Config file Not Found!')
        except KeyError:
            error('Invalid Configs!', 'Required Configs Not Found!')

    def to_dict(self) -> dict:
        return {
            'interval': self.interval,
            'access_token': self.access_token,
            'payload': self.payload,
        }

    def save(self) -> None:
        with open('config.json', '+w') as file:
            file.write(json.dumps(self.to_dict()))


if __name__ == '__main__':
    config = Config()
    print(config.to_dict())
