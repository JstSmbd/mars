from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def index():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
