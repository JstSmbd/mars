from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/training/<string:profession>')
def index(profession):
    return render_template('training.html', profession=profession.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
