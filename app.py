from flask import Flask

app = Flask(__name__)

@app.route("/")
def new_dawn_new_day():
    return 'new dawn, new day'

if __name__ == '__main__':
    app.run(host='127.0.0.1')