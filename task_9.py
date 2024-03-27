from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/accessories/')
def accessories():
    context = {'title': 'Аксессуары'}
    return render_template('accessories.html', **context)


if __name__ == '__main__':
    app.run()


