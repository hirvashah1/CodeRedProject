from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bar')
def bar():
	name = request.args.get('name')
	return "Your name is " + name

if __name__ == '__main__':
	app.run()
