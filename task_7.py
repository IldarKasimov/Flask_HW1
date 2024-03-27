from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    news = [
        {
            'title_new': 'Politics',
            'description': 'In the UK made a shocking statement about nuclear weapons',
            'date': '2024.01.27'
        },
        {
            'title_new': 'Sport',
            'description': 'Germany calls for drone ban during Euro 2024',
            'date': '2024.03.25'
        },
        {
            'title_new': 'Culture',
            'description': 'Kusturica will begin preparations for the filming of '
                           '"Crimes without punishment" in the fall',
            'date': '2024.02.27'
        }
    ]
    context = {'list_news': news,
               'title': 'NEWS'}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()