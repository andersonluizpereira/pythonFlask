from flask import Flask, redirect, url_for

app = Flask(__name__, static_folder='public')



if __name__ == '__main__':
    app.run()