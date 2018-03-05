from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def home_page():
	"""The home page."""
	

	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
