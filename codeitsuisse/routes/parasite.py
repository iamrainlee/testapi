import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    result = []
    for i in data:
        result.append(calparasite(i))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def calparasite(data):
    r = {}
    r["room"] = data["room"]
    r["p1"] = {}
    for i in data['interestedIndividuals']:
        r["p1"][i] = -1
    r["p2"] = 1
    r["p3"] = 1
    r["p4"] = 0
