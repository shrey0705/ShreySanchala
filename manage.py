from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello and Welcome World!'

if __name__ == "__main__":
	app.run

@app.route('/christmas')
def merry_christmas():
	return 'Merry Christimas!'

@app.route ('/newyear')
def new_year():
	return 'Happy New Year!'

