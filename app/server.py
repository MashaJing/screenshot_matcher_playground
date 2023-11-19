from flask import Flask, send_file

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def get_main():
    return send_file('main.html')


@app.route('/media/Lancer.png', methods = ['GET'])
def get_image():
    return send_file('media/Lancer.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)