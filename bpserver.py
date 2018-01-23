from flask import Flask
from flask import request, abort
from bpdata import CaptureType
from bpdata import get_new_session, persist_record

app = Flask(__name__)


def main():
    app.run()


@app.route("/")
def home():
    return "alive"


@app.route("/bpr", methods=['POST'])
def add_bpr():
    payload = request.json
    print(payload)
    return "posted"


@app.route("/capturetype", methods=['POST'])
def add_capture_type():
    if not request.json:
        abort(400)
    capture_type = request.json
    capture_type_record = CaptureType(capture_type['description'])
    print(capture_type_record.json_string())
    session = get_new_session('bprecords.db')
    persist_record(session, capture_type_record)
    return "posted new capture type {}".format(capture_type_record.json_string())


if __name__ == "__main__":
    main()
