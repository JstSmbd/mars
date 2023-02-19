import os

from flask import Flask, url_for, request
from random import choice
import requests
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
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
                <title>Отбор астронавтов</title>
              </head>
              <body>
                <h1 class="center">Загрузка фотографии</h1>
                <div class="center">для участия в миссии</div>
                    <form class="login_form" method="post" enctype="multipart/form-data">
                        <div>Приложите фотографию</div>
                        <div class="form-group">
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <img src="{url_for('static', filename='img/picture.png')}" alt="">
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
              </body>
            </html>'''
    elif request.method == 'POST':
        request.files['file'].save("static/img/picture.png")
        try:
            im = Image.open("static/img/picture.png")
            if im.size[0] > 430:
                percent = 430 / im.size[0]
                im = im.resize((int(im.size[0] * percent), int(im.size[1] * percent)))
            im.save("static/img/picture.png")
        except UnidentifiedImageError:
            pass
        return requests.get("http://127.0.0.1:8080/load_photo").content


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    if os.path.exists("static/img/picture.png"):
        os.remove("static/img/picture.png")
