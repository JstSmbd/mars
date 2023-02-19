from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, BooleanField, SubmitField, FieldList
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<string:le>/<int:age>')
def main(le, age):
    return render_template('training.html', title='Цвет каюты',
                           color=f"{'light' if age < 21 else ''}"
                                 f"{'red' if le == 'female' else 'blue'}.png",
                           picture="young.png" if age < 21 else "old.png")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
