# -*- coding: utf-8 -*-
import os
import time
from flask import Flask


app = Flask(__name__)


@app.route('/health/')
def health():
    return '{"status": "OK"}'


@app.route('/version/')
def version():
    return '{"version": "0.2"}'


@app.route('/')
def hello():
    return 'Hello world from ' + os.environ.get("HOSTNAME", "localhost") + "!"


if __name__ == "__main__":
    time.sleep(1)
    app.run(host="0.0.0.0", port="8000")
