from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class AddPhoto(FlaskForm):
    file = FileField("Добавить картинку", validators=[DataRequired()])
    submit = SubmitField("Отправить")


@app.route('/galery', methods=["GET", "POST"])
def main():
    form = AddPhoto()
    if request.files:
        request.files["file"].save(f"static/img/p{int(names[-1][1:]) + 1}.jpg")
        names.append(f"p{int(names[-1][1:]) + 1}")
    return render_template('training.html', title="Красная планета", names=names, form=form)


names = ["p1", "p2", "p3", "p4"]
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
