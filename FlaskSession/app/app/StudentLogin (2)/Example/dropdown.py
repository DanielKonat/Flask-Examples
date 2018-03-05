from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    return render_template('drop.html')

if __name__ == "__main__":
    app.run()
