from flask import Flask
from requests import get
from time import time

app = Flask(__name__)

@app.route("/freeclash/<protocol>")
def main(protocol):
    return get(f"https://www.freeclash.top/v1/sub/{protocol}/{int(time())}").content
