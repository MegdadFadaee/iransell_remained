from LabelWindow import LabelWindow
from requests import request, Response
from config import Url, Config, error

config = Config()
headers = {
    'Accept-Language': 'fa',
    'Authorization': config.access_token,
}


class Window(LabelWindow):
    def text_schedule(self):
        try:
            remained = get_remained_data()
        except KeyError:
            refresh_tokens()
            remained = get_remained_data()

        self.text(remained)


def load_token() -> Response:
    return request('POST', Url.post_token(), headers=headers, json=config.payload)


def load_remained() -> Response:
    return request('GET', Url.get_account(), headers=headers)


def refresh_tokens() -> None:
    json: dict = load_token().json()
    try:
        access_token: str = json['access_token']
        refresh_token: str = json['refresh_token']

        config.access_token = access_token
        config.payload['refresh_token'] = refresh_token
        config.save()
    except KeyError:
        error('Token Refresh!', 'We could not refresh your token,\nmaybe because of wrong configs.')


def get_remained_data() -> int:
    json: dict = load_remained().json()
    remained: list = json.get('cumulative_amounts', [])
    for data in remained:
        if data.get('type') == 'data':
            return int(data.get('remained'))
    return 0


if __name__ == '__main__':
    app = Window()
    app.interval = config.interval
    app.mainloop()
