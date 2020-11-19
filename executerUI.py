from flask import Flask, render_template
from flask import request
from flask_material import Material

from executer import executer

app = Flask(__name__)
Material(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        code = request.form['code']
        print("CÓDIGO:\n",code)
        printed = executer(code)
        print("RESULTADO:\n",printed)
        return render_template('index.html',result=printed,coded=code)
    else:
        return render_template('index.html')


if __name__=='__main__':
    app.run(use_reloader = True,debug = True, host= '0.0.0.0', port=8080)