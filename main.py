from tkinter import messagebox
from requests import get, Response
from LabelWindow import LabelWindow
from config import Url, headers, interval


class Window(LabelWindow):
    def text_schedule(self):
        response = load_remained()
        remained = find_remained_data(response)
        self.text(remained)

        super().text_schedule()


def load_remained() -> Response:
    return get(Url.get_account(), headers=headers)


def find_remained_data(response: Response) -> int:
    json: dict = response.json()
    try:
        remained: list = json['cumulative_amounts']
        data: dict = next(d for d in remained if d['type'] == 'data')
        return int(data['remained'])
    except KeyError:
        print(response.text)
        messagebox.showerror('Invalid Token!', json['detail'])
        exit(0)


if __name__ == '__main__':
    app = Window()
    app.interval = interval
    app.mainloop()
