from flask import Flask
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)
#1. The example with user
@app.route('/hello/<user>')
def user(user):
    return 'Hello, user: ' + user


#2. addition of two numbers
@app.route('/add/<number_1>/<number_2>')
def addtion(number_1, number_2):
    return str(int(number_1) + int(number_2))


#3. choosing the string with max lenth
@app.route('/max_lenth/<str_1>/<str_2>/<str_3>')
def maximum(str_1, str_2, str_3):
    dict = {len(str_1):str_1, len(str_2):str_2, len(str_3):str_3}
    return dict[max(dict)]


#4. checking of file's existance
@app.route('/existance/<path>')
def does_file_exist(path):
    dir_name =  r'C:/Иван/Python/New homework/8/'
    filename = dir_name + path
    try:
        f = open(filename)
        f.close()
        return 'File exists! ' + filename
    except FileNotFoundError:
        return 'File does not exist! ' + filename


if __name__ == '__main__':
    app.run()