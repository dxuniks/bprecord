import json
from flask import Flask
from flask import request, abort
from bpdata import CaptureType
from bpdata import get_new_session, persist_record

app = Flask(__name__)

session = None

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

@app.route("/capturetype", methods=['GET'])
def get_capture_type():
    global session
    if session is None:
        session = get_new_session('bprecords.db')
    capture_type_list = []
    for capture_type in session.query(CaptureType):
        capture_type_list.append(capture_type.to_json())
    return json.dumps(capture_type_list)

@app.route("/capturetype", methods=['POST'])
def add_capture_type():
    if not request.json:
        abort(400)
    capture_type = request.json
    capture_type_record = CaptureType(capture_type['description'])
    print(capture_type_record.json_string())
    global session
    if session is None:
       session = get_new_session('bprecords.db')
    persist_record(session, capture_type_record)
    return "posted new capture type {}".format(capture_type_record.json_string())


if __name__ == "__main__":
    main()
