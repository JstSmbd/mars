from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/login', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('training.html', title="Аварийный доступ")
    elif request.method == "POST":
        if request.form.get("id2", "") in passwords["captains"] and \
                request.form.get("pas2", "") == passwords["captains"][request.form.get("id2", "")] \
                and request.form.get("id1", "") in passwords["usually"] and \
                request.form.get("pas1", "") == passwords["usually"][request.form.get("id1", "")]:
            return "Вы успешно получили доступ"
        else:
            return "Что-то не так"


passwords = {"captains": {"24": "123"}, "usually": {"1": "qwerty", "563": "456", "78": "hello"}}
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
