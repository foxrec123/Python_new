from flask import Flask
import json

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

#1. По адресу /locales должен возвращаться массив в формате json с тремя локалями:
# ['ru', 'en', 'it']
@app.route('/locales')
def locales():
    return json.dumps({
        'Russian':'ru',
        'English':'en',
        'Italian':'it'
    })


if __name__ == '__main__':
    app.run()