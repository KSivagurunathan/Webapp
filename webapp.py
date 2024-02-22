from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'My webapp v1 '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
