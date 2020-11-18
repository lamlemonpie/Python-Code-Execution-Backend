from flask import Flask, render_template
from flask import request
from flask_material import Material

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return 'POST'
    else:
        return render_template('index.html')


if __name__=='__main__':
    app.run(use_reloader = True,debug = True, host= '0.0.0.0', port=8080)