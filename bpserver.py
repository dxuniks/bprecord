from flask import Flask
from flask import request

app = Flask(__name__)


def main():
    app.run()

@app.route("/")
def home():
    return "alive"

@app.route("/bpr", methods=['POST'])
def add_bpr():
    payload = request.data
    print (payload)
    return "posted"

if __name__ == "__main__":
    main()