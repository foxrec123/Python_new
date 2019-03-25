from flask import Flask, request
import json
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, ValidationError

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

class ContactForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=6, max=35),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


#1. По адресу /locales должен возвращаться массив в формате json с тремя локалями:
# ['ru', 'en', 'it']
@app.route('/locales')
def locales():
    return json.dumps({
        'Russian':'ru',
        'English':'en',
        'Italian':'it'
    })

#2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа,
# возвращать их сумму
@app.route('/sum/<first>/<second>')
def add(first, second):
    return str(int(first) + int(second))

#4. По адресу /form/user должен принимать POST запрос с параментрами:
# email, пароль и подтверждение пароля. Необходимо валидировать email,
# что обязательно присутствует, валидировать пароли, что они минимум 6 символов
# в длину и совпадают. Возрващать пользователю json вида:

@app.route('/form/user',  methods=['POST'])
def home():
    if request.method == 'POST':
        form = ContactForm(request.form)

        response = {}
        if form.validate():
            response['status'] = 1
            response['errors'] = ''
        else:
            response['status'] = 0
            response['errors'] = form.errors

        return json.dumps(response, indent=4)


#5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого
# файла из папки ./files.
#Файлы можно туда положить любые текстовые. А если такого нет - 404.
@app.route('/serve/<path:filename>')
def files(filename):
    path = r'D:/Books/' + filename
    print(path)
    try:
        f = open(path)
        content = f.read()
        f.close()
        return content
    except:
        return '404'

if __name__ == '__main__':
    app.run()