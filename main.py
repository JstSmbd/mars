from flask import Flask, url_for, request, render_template, redirect
import json


app = Flask(__name__)


@app.route('/member')
def main():
    with open("templates/people.json", "rt", encoding="utf8") as f:
        people_list = json.loads(f.read())
    return render_template('training.html', title="Личная карточка", people=people_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
