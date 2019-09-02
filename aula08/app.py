from flask import Flask, request,redirect, url_for
import json
app = Flask(__name__, static_folder='public')

@app.route("/", methods=["GET","POST"])
def index():
    print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps(t1)

if __name__ == '__main__':
    app.run()