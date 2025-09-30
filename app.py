from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask is up and running!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)  # nosec B104
