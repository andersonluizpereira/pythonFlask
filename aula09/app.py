from flask import Flask, request,redirect, url_for,abort
import json
app = Flask(__name__, static_folder='static')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['pass'] == 'admin':
            return redirect(url_for('sucesso'), code=200)
        else:
            abort(401)

    else:
        abort(403)

@app.route('/sucesso')
def sucesso():
    return 'sucesso'

if __name__ == '__main__':
    app.run()