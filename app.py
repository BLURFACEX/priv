from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Pal ECS Container."

if __name__ == '__main__':
    # Listen on all available interfaces, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
