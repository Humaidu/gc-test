from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/<username>')
def about(username):
    return render_template('about.html', name=username)


if __name__ == '__main__':
    app.run(debug=True)