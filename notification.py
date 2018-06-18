import requests

from utils import get_env

apikey = get_env('mailgun_apikey')


def send_notification(email, text):
    r = requests.post(
        'https://api.mailgun.net/v3/pypi-mirrors.org/messages',
        auth=('api', apikey), data={
            'from': 'webmaster <postmaster@pypi-mirrors.org>',
            'to': email,
            'subject': 'You have new un/follows',
            'text': text,
        })
    print(r.text)
    return r.status_code == 200


if __name__ == '__main__':
    send_notification('akabyw@gmail.com', 'test')
