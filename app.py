from flask import Flask, render_template

IMG_DIR = './static'

app = Flask(__name__)

# a handler that returns a message on the '/' page!
@app.route("/")
def serve_text():
    return 'new dawn, new day'

# a handler that returns an html file with an image!
@app.route("/image")
def serve_image():
    return render_template('image.html')

# start the application
if __name__ == '__main__':
    app.run(host='127.0.0.1')