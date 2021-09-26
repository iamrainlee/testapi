import logging
import json
import copy
import math
import hashlib

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/cipher-cracking', methods=['POST'])
def ciphercracking():
    data = request.get_json()
    logging.info("Data: {}".format(data))
    # result = []
    # for i in data:
    #     result.append(calstonks(i))
    D = data[0]["D"]
    X = data[0]["X"]
    Y = data[0]["Y"]
    mins = data[0]["est_mins"]
    result = []
    for i in range(1,pow(10,D)):
        if(hashlib.sha256(i)==Y):
            result.append(i)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
