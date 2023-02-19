import os
import sys
import pygame
from flask import Flask, url_for, request
from PIL import Image
app = Flask(__name__)


@app.route('/carousel')
def sample_file_upload():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                             <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                             <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                             <title>Пейзажи Марса</title>
                             <div id="carousel" class="carousel slide" data-ride="carousel">
                              <div class="carousel-inner">
                                {"".join([f'''<div class='carousel-item{" active" if i == 1 else ""}'>
                                  <img src='{url_for('static', filename=f'img/r{i}.jpg')}'>
                                </div>''' for i in range(1, 5)])}
                              </div>
                              <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                              </a>
                              <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                              </a>
                             </div>"""


def set_size(file, file2, w, h):
    im1 = Image.open(file)
    im2 = Image.new("RGB", (w, h), (255, 133, 0))
    im2.paste(im1, ((im2.size[0] - im1.size[0]) // 2, (im2.size[1] - im1.size[1]) // 2))
    im2.save(file2)


if __name__ == '__main__':
    pygame.init()
    for i in range(1, 5):
        set_size(f"static/img/p{i}.jpg", f"static/img/r{i}.jpg",
                 pygame.display.Info().current_w, pygame.display.Info().current_h)
    app.run(port=8080, host='127.0.0.1')
