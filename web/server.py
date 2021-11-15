from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('class-1.html')

@app.route('/args/<name>')
def hello_with_args(name):
    data = {
        'name': name,
        'studentId': 202014141414
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()