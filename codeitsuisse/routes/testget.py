#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/testget', methods=['GET'])
def testget():
    rdata = {}
    if(len(request.args)>0 and request.args.get("action") is not None):
        data = request.args
        if(data["action"] == "get_students"):
            if(request.args.get("name") is None):
                rdata = json.loads('[{"Name":"Nicole","UID":"3035785611","DOB":"2002-11-08","Local":"TRUE","Beautiful Index":1000},{"Name":"Rain","UID":"3035779571","DOB":"2002-04-05","Local":"TRUE","Beautiful Index":"NULL"}]')
            else:
                if(data["name"] == "Nicole"):
                    rdata = json.loads('{"Name":"Nicole","UID":"3035785611","DOB":"2002-11-08","Local":"TRUE","Beautiful Index":1000}')
                elif(data["name"] == "Rain"):
                    rdata = json.loads('{"Name":"Rain","UID":"3035779571","DOB":"2002-04-05","Local":"TRUE","Beautiful Index":"NULL"}')
                else:
                    rdata["error"] = "Student not found"
        else:
            rdata["error"] = "Wrong action"
    else:
        rdata["error"] = "Missing parameters"
    return jsonify(rdata)
