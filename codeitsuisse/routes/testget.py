#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/testget', methods=['GET'])
def testget():
    data = request.args
    rdata = {}
    if(data["action"] == "get_students"):
        rdata = json.loads('[{"Name":"Nicole","UID":"3035785611","DOB":"2002-11-08","Local":"TRUE","Beautiful Index":1000},{"Name":"Rain","UID":"3035779571","DOB":"2002-04-05","Local":"TRUE","Beautiful Index":"NULL"}]')
    else:
        rdata["error"] = "Missing action"
    return json.dumps(rdata)
