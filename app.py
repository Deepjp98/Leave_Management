from flask import Flask
from flask import request, jsonify, flash, g
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import json
app = Flask(__name__)
import numpy as np
import  leave_register
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "Log"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
file_handler.setFormatter(FORMATTER)
logger.addHandler(file_handler)
logger.propagate = False

@app.route('/leavemanagement/welcome')
def hello_world():
    return 'Welcome to Leave management framework!'

@app.route('/leavemanagement/login')
def login():
    return ""

@app.route('/leavemanagement/ragister' , methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            if "application/json" == request.headers["Content-Type"]:
                status, msg = leave_register.validate(request)
                if status == False:
                    response = app.response_class(
                        response=json.dumps({'message': msg}, default=np_encoder, indent=4),
                        mimetype='application/json'
                    )
                    return response
                # master = request.json["master_id"]
                try:
                    data = leave_register.createSuperUSer(request)
                    response = app.response_class(
                        response=json.dumps("{'message': 'success'}" , default=np_encoder,indent=4),
                        mimetype='application/json'
                    )
                    return response
                except Exception as e:
                    print(str(e))

        except Exception as e:
            print(str(e))
            response = app.response_class(
                response=json.dumps({'message': 'must be pass valid json'}, default=np_encoder, indent=4),
                mimetype='application/json'
            )
            return response
def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)