from flask import Flask, url_for, request
from random import choice

app = Flask(__name__)


@app.route('/choice/<planet>', methods=["POST", "GET"])
def main(planet):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    {planets.get(planet.lower(), "<div>Планеты {planet} не найдено</div>").format(planet=planet)}
                  </body>
                </html>'''


with app.app_context(), app.test_request_context():
    alerts = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
    templates = ['<h1>Мое предложение: {planet}</h1>',
                 '''<div class="alert alert-{choice_color}">
                          <div class={choice_font}>{text}</div>
                          </div>''',
                 "<img src='{image}' alt='здесь должна была быть картинка, но не нашлась'>"]
    planets = {
        "марс": templates[0] + templates[2].format(
            image=url_for('static', filename="img/mars.png")) +
                "".join([templates[1].format(choice_color=choice(alerts),
                                             choice_font=choice(
                                                 ["bold", "italic",
                                                  "oblique", "line"]),
                                             text=text, planet="{planet}")
                         for text in ["Эта планета близка к Земле;",
                                      "На ней много необходимых ресурсов;",
                                      "На ней есть вода и атмосфера;",
                                      "На ней есть небольшое магнитное поле;",
                                      "Наконец, она просто красива!"]]),
        "луна": templates[0] + "".join([templates[1].format(choice_color=choice(alerts),
                                                            choice_font=choice(
                                                                ["bold", "italic",
                                                                 "oblique", "line"]),
                                                            text=text, planet="{planet}")
                                        for text in ["Луна является спутником Земли;",
                                                     "Она в 50 раз меньше Земли по объему;",
                                                     "У Луны нет магнитного поля;",
                                                     "12 человек уже побывало на Луне;",
                                                     "Скоро будет и наша очередь!"]]),
        "юпитер": templates[0] +
                  templates[2].format(image=url_for('static', filename="img/jupiter.png"))
                  + "<div class='bold'>Самая большая планета в Солнечной системе</div>"}

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
