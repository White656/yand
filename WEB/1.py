from flask import Flask, render_template
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def odd_even():
    return render_template('base.html')


@app.route('/list_prof/<lis>')
def odd(lis):
    z = ["Инженер", "Медик", "Пилот"]
    return render_template('test.html', name=lis, prof=z)


if __name__ == '__main__':
    app.run(port=f"80{random.randint(1, 9)}0", host='127.0.0.1')
