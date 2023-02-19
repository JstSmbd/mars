from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/list_prof/<string:mode>')
def index(mode):
    return render_template('training.html', mode=mode,
                           professions=["инженер-исследователь", "пилот", "строитель", "экзобиолог",
                                        "врач", "инженер по терраформированию", "климатолог",
                                        "специалист по радиационной защите", "астрогеолог",
                                        "гляциолог", "инженер жизнеобеспечения", "метеоролог",
                                        "оператор марсохода", "киберинженер", "штурман",
                                        "пилот дронов"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
